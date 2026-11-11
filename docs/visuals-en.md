# GitHub visual previews

[Deutsch](visuals-de.md) · [Home](../README.md)

The README uses PNGs because they render directly on GitHub without requiring visitors to run a skill or open a diagram editor. Each image has alternative text in the README and links back to the documented examples.

| Preview | Actual source and meaning |
| --- | --- |
| Fraction | Canonical helper's SVG for 11/12: eleven shaded parts of one whole, twelve equal parts in total |
| Quadratic | Canonical helper's SVG for x²−4x+3: roots 1 and 3, vertex (2,−1); numerical plot with labeled scales |
| Complex roots | Canonical helper's SVG for z³=8i: three roots on a circle of radius 2, equal axis scales |
| ER | Graphviz drawing of the relationships in examples/enrollment.json; labels count instances at each endpoint; helper itself exports Mermaid source |
| XML | The unmodified tree text from examples/xml-en.md, placed in a readable image; no element text or attribute values |
| Formulas | Matplotlib MathText rendering of formulas used in the original examples; not a screenshot of a compiled LaTeX worksheet |
| Overview | A composite of the six previews, with project title and the student-led motto |

No preview is presented as a screenshot of Claude or an interactive application. Math plots are numerical views; exact reasoning remains in the examples. The ER drawing states assumptions rather than inventing course requirements. Full-size PNGs and original SVG/XML/JSON/TeX sources are included.

## Regenerate images

Optional documentation dependencies: Python with Pillow and Matplotlib, plus Inkscape and Graphviz (`dot`) on PATH. These are **not runtime requirements** of the installed skills or study helpers. The script uses DejaVu Sans fonts when available.

From the repository root:

```bash
python3 scripts/build_previews.py
```

This rebuilds all 14 EN/DE PNGs under docs/images from the bundled examples and labels. After changing example data, review the diagram relationships and captions too. Inspect the regenerated images and run `python3 scripts/validate_repo.py` to check local image links before committing.
