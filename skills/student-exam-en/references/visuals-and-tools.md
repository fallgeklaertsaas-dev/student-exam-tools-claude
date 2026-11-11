# Visuals and offline tools

Use the installed skill's absolute path in place of SKILL_DIR. Do not type that placeholder literally. Commands below require Python 3.10+ and no dependencies. Each `--output` path must be new; parent directories must exist. Omit `--output` to emit source to stdout. Use `python` instead of `python3` on Windows if that is the available command.

```bash
python3 SKILL_DIR/scripts/study_tools.py fraction 11 12 --lang en --output fraction.svg
python3 SKILL_DIR/scripts/study_tools.py quadratic 1 -4 3 --lang en --output parabola.svg
python3 SKILL_DIR/scripts/study_tools.py quadratic 1 -4 3 --analysis
python3 SKILL_DIR/scripts/study_tools.py complex-roots 0 8 3 --lang en --output complex.svg
python3 SKILL_DIR/scripts/study_tools.py er model.json --output model.mmd
python3 SKILL_DIR/scripts/study_tools.py xml course.xml --lang en --output tree.md
```

Supported fraction range: denominator 1..24; numerator 0..5×denominator, integers only. Equal-width cells show equal parts. Negative fractions need a number line or text instead.

Quadratic coefficients must be finite, absolute value ≤10⁶ and |a|≥10⁻⁹. The domain window defaults to [−5,5]; use `--xmin`/`--xmax` to change it. The graph includes numeric axis scales and the zero baseline, and reports real roots and the vertex as numerical approximations. It does not produce complex roots. Highly unequal axis scales may flatten details; choose a better interval and explain this limitation.

The `complex-roots real imag degree` helper plots numerical solutions of z^degree=real+imag*i on equally scaled axes. Degree range: 1..12; finite components with absolute value ≤10⁶. `--analysis` emits coordinates as JSON. Zero has one distinct root with multiplicity equal to the degree; do not present it as several distinct roots. Use exact algebra separately when available. Quadratic discriminants use the displayed decimal coefficients for the sign decision; results remain numerical. Inputs below the representable discriminant range are rejected rather than treated as double roots. Negative scientific literals such as `-1e-5` are supported.

## ER input contract

```json
{
  "entities": ["Student", "Enrollment"],
  "relationships": [{
    "a": "Student", "b": "Enrollment", "label": "has",
    "a_to_b": {"min": 0, "max": "many"},
    "b_to_a": {"min": 1, "max": 1}
  }]
}
```

`a_to_b` counts B for one A. The output places that multiplicity beside B. Use ASCII entity identifiers beginning with a letter; labels may include Unicode words but no diagram directives or quotes. The helper checks structure, not the truth of the model. Keep conceptual attributes and identifying relationships in another explicitly chosen notation if needed.

## LaTeX and accessible delivery

Use `\(...\)` for inline mathematics and `\[...\]` for display mathematics in host chat when supported; GitHub Markdown examples use `$...$` and `$$...$$`. A source-only host may need fenced `latex` instead. Do not claim renderer compatibility without testing. For standalone LaTeX, include `\documentclass`, required packages and `\begin{document}`. Never compile untrusted TeX with shell escape. Provide source when a TeX engine is unavailable.

SVG includes a title and description; pair it with a plain explanation. Mermaid `.mmd` files are source, not rendered images. Place their content in a fenced `mermaid` block on a supporting host. XML trees are text outlines. Exporting PDF or interactive HTML is outside these helpers; use an available trusted host tool if requested and verify the result.

Reserved Mermaid identifiers (including `erDiagram`, `direction` and `classDef`) and directive-like labels such as `direction LR` are rejected; choose a descriptive entity name instead.
