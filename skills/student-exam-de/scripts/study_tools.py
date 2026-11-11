"""Small, offline educational renderers. No expression evaluation or network access."""
from __future__ import annotations

import argparse
import cmath
from fractions import Fraction
from html import escape
import json
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

VERSION = "0.1.0"
MAX_INPUT = 200_000
TEXT = {
    "en": {"fraction": "Fraction model", "shaded": "shaded", "whole": "Parts per whole",
           "parabola": "Quadratic function", "x": "x", "y": "y", "xml": "XML structure",
           "error": "Error", "write": "Wrote", "roots": "Real roots", "none": "none",
           "vertex": "Vertex", "approx": "Numerical approximation"},
    "de": {"fraction": "Bruchmodell", "shaded": "markiert", "whole": "Teile pro Ganzem",
           "parabola": "Quadratische Funktion", "x": "x", "y": "y", "xml": "XML-Struktur",
           "error": "Fehler", "write": "Gespeichert", "roots": "Reelle Nullstellen", "none": "keine",
           "vertex": "Scheitelpunkt", "approx": "Numerische Näherung"},
}


def read_text(path: str) -> str:
    """Bound before decoding; accept UTF-8 only."""
    with Path(path).open("rb") as stream:
        raw = stream.read(MAX_INPUT + 1)
    if len(raw) > MAX_INPUT:
        raise ValueError("Input exceeds 200000 bytes / Eingabe über 200000 Bytes")
    return raw.decode("utf-8")


def svg_document(title: str, description: str, body: str, width=800, height=480) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>\n'
            '<rect width="100%" height="100%" fill="white"/>\n'
            '<g font-family="Arial, sans-serif" font-size="16" fill="#172b4d">\n'
            f'{body}\n</g></svg>\n')


def fraction_svg(numerator: int, denominator: int, lang="en") -> str:
    """Render nonnegative fractions, with equal units on separate bars."""
    if type(numerator) is not int or type(denominator) is not int:
        raise ValueError("Use integers / Ganze Zahlen verwenden")
    if numerator < 0 or denominator < 1 or denominator > 24 or numerator > 5 * denominator:
        raise ValueError("Require 0 <= numerator <= 5*denominator, 1 <= denominator <= 24 / Wertebereich beachten")
    t = TEXT[lang]
    units = max(1, math.ceil(numerator / denominator))
    height = 110 + units * 70
    title = f'{t["fraction"]}: {numerator}/{denominator}'
    reduced = str(Fraction(numerator, denominator))
    desc = f'{numerator}/{denominator} = {reduced}; {t["shaded"]}: {numerator}, {t["whole"]}: {denominator}'
    parts = [f'<text x="28" y="35" font-size="22">{escape(title)} = {escape(reduced)}</text>']
    cell = 660 / denominator
    for unit in range(units):
        for index in range(denominator):
            shade = unit * denominator + index < numerator
            x, y = 28 + index * cell, 65 + unit * 70
            parts.append(f'<rect x="{x:.3f}" y="{y}" width="{cell:.3f}" height="44" '
                         f'fill="{"#245ca6" if shade else "#f1f4f9"}" stroke="#172b4d"/>')
        parts.append(f'<text x="705" y="{94 + unit * 70}">{unit + 1}</text>')
    parts.append(f'<text x="28" y="{height - 12}">{escape(t["whole"])} = {denominator}</text>')
    return svg_document(title, desc, "\n".join(parts), 800, height)


def quadratic_analysis(a: float, b: float, c: float) -> dict:
    """Return finite floating-point results; reject unstable/overflowing inputs."""
    if not all(math.isfinite(v) and abs(v) <= 1e6 for v in (a, b, c)) or abs(a) < 1e-9:
        raise ValueError("Require finite |coefficients| <= 1e6 and |a| >= 1e-9 / Koeffizienten prüfen")
    # Interpret displayed decimal coefficients exactly for the sign decision.
    # A rounding tolerance would incorrectly merge genuinely distinct close roots.
    fa, fb, fc = (Fraction(str(v)) for v in (a, b, c))
    exact_discriminant = fb * fb - 4 * fa * fc
    discriminant = float(exact_discriminant)
    if exact_discriminant and discriminant == 0:
        raise ValueError("Discriminant below floating range / Diskriminante unter Gleitkommagrenze")
    vx = float(-fb / (2 * fa))
    vy = float(-exact_discriminant / (4 * fa))
    if discriminant < 0:
        roots = []
    elif discriminant == 0:
        roots = [vx]
    else:
        # Stable form avoids cancellation for very different roots.
        q = -0.5 * (b + math.copysign(math.sqrt(discriminant), b))
        roots = sorted([q / a, c / q])
    if not all(math.isfinite(v) for v in (discriminant, vx, vy, *roots)):
        raise ValueError("Numerical range exceeded / Numerischer Wertebereich überschritten")
    return {"a": a, "b": b, "c": c, "discriminant": discriminant,
            "vertex": [vx, vy], "real_roots": roots, "approximate": True}


def quadratic_svg(a: float, b: float, c: float, xmin=-5.0, xmax=5.0, lang="en") -> str:
    info = quadratic_analysis(a, b, c)
    if not all(math.isfinite(v) and abs(v) <= 1e6 for v in (xmin, xmax)) or xmax - xmin < 1e-6:
        raise ValueError("Require finite xmin < xmax with width >= 1e-6 / x-Bereich prüfen")
    t = TEXT[lang]
    xs = [xmin + (xmax - xmin) * i / 200 for i in range(201)]
    ys = [(a * x + b) * x + c for x in xs]
    if xmin <= info["vertex"][0] <= xmax:
        ys.append(info["vertex"][1])
    low, high = min(0.0, *ys), max(0.0, *ys)
    pad = max((high - low) * 0.08, 1.0)
    low, high = low - pad, high + pad
    px = lambda x: 80 + 640 * (x - xmin) / (xmax - xmin)
    py = lambda y: 360 - 270 * (y - low) / (high - low)
    expression = ("−" if a < 0 else "") + ("" if abs(a) == 1 else f"{abs(a):g}") + "x²"
    for coefficient, variable in ((b, "x"), (c, "")):
        if coefficient:
            magnitude = "" if variable and abs(coefficient) == 1 else f"{abs(coefficient):g}"
            expression += (" − " if coefficient < 0 else " + ") + magnitude + variable
    title = f'{t["parabola"]}: y = {expression}' 
    roots = ", ".join(f'{v:.6g}' for v in info["real_roots"]) or t["none"]
    vertex = ", ".join(f'{v:.6g}' for v in info["vertex"])
    summary = f'{t["roots"]}: {roots}; {t["vertex"]}: ({vertex})'
    body = [f'<text x="28" y="32" font-size="21">{escape(title)}</text>',
            f'<text x="28" y="60">{escape(t["approx"])}</text>']
    for i in range(6):
        x = xmin + (xmax - xmin) * i / 5
        y = low + (high - low) * i / 5
        body += [f'<path d="M {px(x):.3f} 90 V 360" stroke="#d0d7e2"/>',
                 f'<text x="{px(x):.3f}" y="385" text-anchor="middle">{x:.4g}</text>',
                 f'<path d="M 80 {py(y):.3f} H 720" stroke="#d0d7e2"/>',
                 f'<text x="72" y="{py(y):.3f}" text-anchor="end">{y:.4g}</text>']
    body.append(f'<path d="M 80 {py(0):.3f} H 720" stroke="#172b4d" stroke-width="2"/>')
    if xmin <= 0 <= xmax:
        body.append(f'<path d="M {px(0):.3f} 90 V 360" stroke="#172b4d" stroke-width="2"/>')
    points = " ".join(f'{px(x):.3f},{py((a*x+b)*x+c):.3f}' for x in xs)
    body.append(f'<polyline points="{points}" fill="none" stroke="#245ca6" stroke-width="3"/>')
    body += ['<text x="740" y="385">x</text>', '<text x="18" y="230">y</text>',
             f'<text x="28" y="425">{escape(summary)}</text>',
             f'<text x="28" y="455">x ∈ [{xmin:g}, {xmax:g}]</text>']
    return svg_document(title, summary, "\n".join(body))


def complex_roots(real: float, imag: float, degree: int) -> dict:
    """Numerical distinct roots of z**degree = real + imag*i."""
    if (type(degree) is not int or not 1 <= degree <= 12
            or not all(math.isfinite(v) and abs(v) <= 1e6 for v in (real, imag))):
        raise ValueError("Require degree 1..12 and finite components <= 1e6 / Grad und Komponenten prüfen")
    value = complex(real, imag)
    radius = abs(value) ** (1 / degree)
    if value == 0:
        points = [complex(0, 0)]
    else:
        points = [cmath.rect(radius, (cmath.phase(value) + 2 * math.pi * k) / degree)
                  for k in range(degree)]
    return {"value": [real, imag], "degree": degree, "radius": radius,
            "roots": [[z.real, z.imag] for z in points],
            "multiplicity_if_zero": degree if value == 0 else None, "approximate": True}


def complex_svg(real: float, imag: float, degree: int, lang="en") -> str:
    info = complex_roots(real, imag, degree)
    scale = info["radius"] * 1.35 if info["radius"] > 0 else 1.0
    px = lambda x: 380 + 180 * x / scale
    py = lambda y: 285 - 180 * y / scale
    title = ("Complex roots" if lang == "en" else "Komplexe Wurzeln") + f": z^{degree} = {real:g} + ({imag:g})i"
    coords = "; ".join(f"z{k}=({x:.6g}, {y:.6g})" for k, (x,y) in enumerate(info["roots"]))
    body = [f'<text x="28" y="32" font-size="22">{escape(title)}</text>',
            f'<text x="28" y="60">{escape(TEXT[lang]["approx"])}</text>']
    for ratio in (-1, -.5, 0, .5, 1):
        x = ratio * scale
        body.extend([f'<path d="M {px(x):.3f} 105 V 465 M 200 {py(x):.3f} H 560" stroke="#d0d7e2"/>',
                     f'<text x="{px(x):.3f}" y="490" text-anchor="middle">{x:.4g}</text>',
                     f'<text x="190" y="{py(x):.3f}" text-anchor="end">{x:.4g}</text>'])
    body += ['<path d="M 200 285 H 560 M 380 105 V 465" stroke="#172b4d" stroke-width="2"/>',
             '<text x="580" y="290">Re</text>', '<text x="380" y="95">Im</text>',
             f'<circle cx="380" cy="285" r="{180*info["radius"]/scale:.3f}" fill="none" stroke="#76849a" stroke-dasharray="5 4"/>']
    for k,(x,y) in enumerate(info["roots"]):
        body += [f'<circle cx="{px(x):.3f}" cy="{py(y):.3f}" r="5" fill="#245ca6"/>',
                 f'<text x="{px(x)+9:.3f}" y="{py(y)-9:.3f}">z{k}</text>']
    note = ("Equal axis scales; dashed circle: root modulus." if lang == "en" else
            "Gleiche Achsenskalierung; gestrichelter Kreis: Wurzelbetrag.")
    body.append(f'<text x="28" y="530">{escape(note)}</text>')
    if real == 0 and imag == 0:
        note = (f"One distinct root at zero, multiplicity {degree}." if lang == "en" else
                f"Eine einzige Wurzel bei null, Vielfachheit {degree}.")
        body.append(f'<text x="28" y="560">{escape(note)}</text>')
    return svg_document(title, coords, "\n".join(body), 760, 590)


IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,39}\Z")
RESERVED = {"erdiagram", "direction", "style", "classdef", "class", "acctitle", "accdescr", "title", "end"}
LABEL = re.compile(r"[\w .,:()/\-]{1,80}\Z", re.UNICODE)


def cardinality(value) -> tuple[int, str]:
    if (not isinstance(value, dict) or set(value) != {"min", "max"}
            or type(value["min"]) is not int or value["min"] not in (0, 1)
            or not ((type(value["max"]) is int and value["max"] == 1) or value["max"] == "many")
            or (value["max"] == 1 and value["min"] > 1)):
        raise ValueError("Cardinality requires min=0|1, max=1|many / Kardinalität prüfen")
    return value["min"], value["max"]


def er_mermaid(model: dict) -> str:
    """Render binary non-identifying conceptual relationships.

    a_to_b is the number of B instances for ONE A instance, so its crow's-foot
    symbol belongs NEXT TO B. Numeric minima >1 require another notation.
    """
    if not isinstance(model, dict) or set(model) != {"entities", "relationships"}:
        raise ValueError("Expected entities and relationships / Entitäten und Beziehungen erforderlich")
    entities, relations = model["entities"], model["relationships"]
    if (not isinstance(entities, list) or not 1 <= len(entities) <= 30
            or not all(isinstance(e, str) and IDENTIFIER.fullmatch(e) and e.casefold() not in RESERVED for e in entities)
            or len(set(entities)) != len(entities)):
        raise ValueError("Use 1..30 unique ASCII entity identifiers / Entitätsnamen prüfen")
    if not isinstance(relations, list) or len(relations) > 60:
        raise ValueError("At most 60 relationships / Höchstens 60 Beziehungen")
    lines = ["erDiagram"] + [f"    {e}" for e in entities]
    left = {(0, 1): "|o", (1, 1): "||", (0, "many"): "}o", (1, "many"): "}|"}
    right = {(0, 1): "o|", (1, 1): "||", (0, "many"): "o{", (1, "many"): "|{"}
    for relation in relations:
        if not isinstance(relation, dict) or set(relation) != {"a", "b", "a_to_b", "b_to_a", "label"}:
            raise ValueError("Invalid relationship fields / Beziehungsfelder prüfen")
        a, b, label = relation["a"], relation["b"], relation["label"]
        if not isinstance(a, str) or not isinstance(b, str) or a not in entities or b not in entities:
            raise ValueError("Unknown entity / Unbekannte Entität")
        if (not isinstance(label, str) or not LABEL.fullmatch(label)
                or re.search(r"direction\s+(?:TB|BT|LR|RL)", label, re.IGNORECASE)):
            raise ValueError("Use a plain-text relationship label / Einfachen Beziehungstext verwenden")
        ab, ba = cardinality(relation["a_to_b"]), cardinality(relation["b_to_a"])
        lines.append(f'    {a} {left[ba]}..{right[ab]} {b} : "{label}"')
    return "\n".join(lines) + "\n"


def xml_outline(text: str, lang="en") -> str:
    """Inspect UTF-8 XML without DTDs/entities; preserve namespace URIs.

    Reports a tree outline, NOT XSD validity; omits text/attribute values.
    """
    if len(text.encode("utf-8")) > MAX_INPUT:
        raise ValueError("XML exceeds 200000 bytes / XML zu groß")
    if "<!DOCTYPE" in text.upper() or "<!ENTITY" in text.upper():
        raise ValueError("DTD/entity tokens unsupported, including comments/CDATA / DTD-/Entity-Textmarker nicht unterstützt, auch Kommentare/CDATA")
    root = ET.fromstring(text)
    output = [f'# {TEXT[lang]["xml"]}', '```text']
    stack = [(root, 0)]
    count = 0
    while stack:
        node, depth = stack.pop()
        count += 1
        if depth > 30 or count > 2000:
            raise ValueError("XML depth/node limit exceeded / XML-Strukturlimit überschritten")
        attrs = " ".join("@" + key for key in sorted(node.attrib))
        output.append("  " * depth + node.tag + (f" [{attrs}]" if attrs else ""))
        stack.extend((child, depth + 1) for child in reversed(list(node)))
    output.append('```')
    return "\n".join(output) + "\n"


def write_new(path: str | None, content: str) -> None:
    if path is None:
        sys.stdout.write(content)
    else:
        # Exclusive creation avoids silently overwriting student work.
        with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)


class NumericArgumentParser(argparse.ArgumentParser):
    """Recognize negative scientific literals as values, including positionals."""
    def _parse_optional(self, arg_string):
        if re.fullmatch(r"-(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", arg_string):
            return None
        return super()._parse_optional(arg_string)


def main(argv=None) -> int:
    parser = NumericArgumentParser(description="Student Exam Tools / Visuelle Lernwerkzeuge (EN/DE)")
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("fraction", "quadratic", "complex-roots", "er", "xml"):
        p = sub.add_parser(name)
        p.add_argument("--lang", choices=("en", "de"), default="en")
        p.add_argument("--output", help="New UTF-8 file; stdout if omitted / Neue UTF-8-Datei")
        if name == "fraction":
            p.add_argument("numerator", type=int)
            p.add_argument("denominator", type=int)
        elif name == "quadratic":
            for coefficient in ("a", "b", "c"):
                p.add_argument(coefficient, type=float)
            p.add_argument("--xmin", type=float, default=-5.0)
            p.add_argument("--xmax", type=float, default=5.0)
            p.add_argument("--analysis", action="store_true", help="JSON instead of SVG / JSON statt SVG")
        elif name == "complex-roots":
            p.add_argument("real", type=float)
            p.add_argument("imag", type=float)
            p.add_argument("degree", type=int)
            p.add_argument("--analysis", action="store_true", help="JSON instead of SVG / JSON statt SVG")
        else:
            p.add_argument("input", help="UTF-8 JSON/XML path / Dateipfad")
    args = parser.parse_args(argv)
    try:
        if args.command == "fraction":
            content = fraction_svg(args.numerator, args.denominator, args.lang)
        elif args.command == "quadratic":
            content = (json.dumps(quadratic_analysis(args.a, args.b, args.c), indent=2) + "\n"
                       if args.analysis else quadratic_svg(args.a, args.b, args.c, args.xmin, args.xmax, args.lang))
        elif args.command == "complex-roots":
            content = (json.dumps(complex_roots(args.real, args.imag, args.degree), indent=2) + "\n"
                       if args.analysis else complex_svg(args.real, args.imag, args.degree, args.lang))
        elif args.command == "er":
            content = er_mermaid(json.loads(read_text(args.input)))
        else:
            content = xml_outline(read_text(args.input), args.lang)
        write_new(args.output, content)
    except (ValueError, OSError, UnicodeError, ET.ParseError, RecursionError) as exc:
        print(f'{TEXT[args.lang]["error"]}: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
