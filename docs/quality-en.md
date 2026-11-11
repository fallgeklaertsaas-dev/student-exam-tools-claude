# Verification and limits — English

[Deutsch](quality-de.md) · [Home](../README.md)

Reviewed on **2026-11-11**, using Python **3.12.14**. This records actual checks, not a claim of perfection or a measured improvement in exam performance.

## Three review passes

| Pass | Actual checks | Result / changes |
| --- | --- | --- |
| 1. Technical and packaging | Executed unit/property-style tests; ran both portable scripts outside the repository; built deterministic ZIPs; checked paths, Python syntax, metadata, links and byte-for-byte helper parity | All 54 test methods pass, including 150 seeded quadratic cases and all 16 endpoint combinations. Installable ZIPs have one matching root and carry the MIT license. |
| 2. Mathematical, bilingual and adversarial review | Checked original-equation fixtures, EN/DE behavior and documentation claims; independent read-only reviewer exercised numeric/CLI edge cases and tested a temporary wheel installation | Fixed decimal double-root classification and negative scientific-literal parsing; added regression tests. Fixed small-root plot scaling. XML's conservative rejection of declaration tokens in comments/CDATA is documented and tested. |
| 3. Learning workflow and visual review | A separate agent used the DE skill on five learner tasks; generated/inspected SVG renderings; reviewed hint boundaries, ER uncertainty, complex roots and namespace explanation | Hint did not spoil the result; unsupported (2,n) was not silently weakened; cube roots included checks; XML namespaces were distinguished. Fraction, quadratic and complex-plane examples were rendered with Inkscape and visually inspected. |

The five-task run used another coding assistant, **not Claude**. It is a small qualitative forward test, not a representative user study or a live-Claude benchmark. The independent reviewer also ran 1,200 random complex-root cases with small original-equation residuals; this is numerical checking, not a proof of all floating-point behavior. See [review notes](../evals/review-notes.md).

## Reproduce the automated checks

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_skills.py
python3 scripts/validate_repo.py
```

Run `build_skills.py` twice and compare `dist/SHA256SUMS.json` to check deterministic output. Both language bundles contain the same canonical Python bytes; only instructions and reference prose differ. A wheel from the reviewed source was built and installed in an isolated temporary target during review. This does not claim PyPI publication.

## Published GitHub verification

The [GitHub Actions run](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude/actions/runs/42990003219) completed successfully for commit `131d851` on Python 3.10, 3.12 and 3.13. Each job ran all 54 tests, rebuilt the two skill archives and validated the repository. The bilingual gallery contains 14 PNGs; source image links and the uploaded overview were verified. This checks code and packaging, not live Claude behavior.

## What remains unverified

- Installation and actual model behavior in Claude web/desktop and local Claude Code. No Claude account session or API key was available. The 20 bilingual behavioral cases are defined, but the full with/without-skill Claude evaluation has **not been run**.
- TeX compilation: both worksheet attempts were blocked because `pdflatex.fmt` is missing in this environment. The `.tex` files are source deliverables, not verified PDFs.
- Mermaid rendering across host versions. Syntax and cardinality mapping are checked; a rendered Mermaid release screenshot is not included.
- Learning outcomes, all school curricula, arbitrary mathematical expressions, general symbolic integration, XSD validation, identifying/ternary ER relationships and all accessibility technology combinations.

## Behavioral evaluation protocol

Use `evals/cases.json` and copy `evals/result-template.json` per trial. For each language, compare a fresh conversation with the skill enabled against the same prompt without it. Record host, model/version, date, tool permissions and the complete observable response. Run at least three trials per condition before drawing conclusions; keep failures. Grade each `must` and `must_not` criterion explicitly, rather than scoring style alone. Do not invent missing records or infer success from a code test.

Publish anonymized results with clear caveats after obtaining appropriate permission. Treat confusing hints, wrong cardinalities and unsupported correctness claims as bugs even if code tests pass.
