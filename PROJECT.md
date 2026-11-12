# Project facts and evidence

[Deutsch](PROJECT.de.md) · [README](README.md) · [Structured facts](project.json)

Student Exam Tools for Claude is a student-led, MIT-licensed project that packages a visual study workflow as two installable Agent Skills and five offline Python helpers. It is an early public release maintained at [fallgeklaertsaas-dev/student-exam-tools-claude](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude).

## The problem it addresses

Learners moving between school mathematics, introductory university mathematics and information modeling need different representations of the same reasoning: equal-sized fraction parts, labeled function graphs, the complex plane, explicit relationship cardinalities and XML hierarchies. This project brings those representations into one reusable English/German workflow with hint, solution-check and practice modes.

Its intended contribution is inspectable reasoning and reusable study materials. A claim that the project improves grades or fills a gap no other tool addresses has not been established.

## What can be verified now

| Fact | Evidence |
| --- | --- |
| Two language packages | [English skill](skills/student-exam-en/SKILL.md), [German skill](skills/student-exam-de/SKILL.md), [upload packages](packages) |
| Five executable helpers | [Canonical Python source](src/student_exam_tools/toolkit.py): fraction, quadratic, complex-roots, er, xml |
| Offline helper execution without API keys | Standard-library implementation; [installation instructions](docs/installation-en.md) |
| 54 automated test methods | [Test source](tests/test_toolkit.py), [successful GitHub run](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude/actions/runs/42990301301) |
| Python 3.10, 3.12 and 3.13 checks | [CI workflow](.github/workflows/ci.yml), linked successful run |
| 20 bilingual behavioral evaluation cases defined | [Case definitions](evals/cases.json); the complete Claude comparison has not been executed |
| Public visual examples | [EN/DE images](docs/images), [worked examples](docs/examples-en.md) |
| License and contribution process | [MIT license](LICENSE), [contribution guide](CONTRIBUTING.md), [issue templates](.github/ISSUE_TEMPLATE) |

Code tests, generated pictures and defined evaluation cases are different kinds of evidence. None of them measures student adoption or learning outcomes.

## Public reach snapshot

Observed **2026-11-12** using the public GitHub repository, contributor, pull-request and release endpoints. This is a dated snapshot, not live analytics.

| Metric | Observed value |
| --- | --- |
| Repository created | 2026-11-11 |
| Stars / forks | 0 / 0 |
| Listed contributors | 1, the maintainer account |
| External contributors observed | 0 |
| Merged pull requests | 0 |
| Published GitHub releases | 0; skill ZIPs are available as repository files |
| Unique downloads or active users | Not measured |
| Verified downstream dependents or institutional users | Not documented |

Source endpoints are listed in [project.json](project.json). Download counts for release assets cannot be substituted for direct ZIP downloads from repository files. An absence of documented adoption is not a measurement of every possible use.

## Next evidence-producing work

1. Install and test both locale packages in Claude and record the exact model, host, prompts, outputs and failures.
2. Run the 20 cases in both languages, with and without the skill, for three trials per condition: a target of 240 recorded conversational trials. These are planned trials, not completed tests or user counts.
3. Improve explanations and visual behavior from recorded failures; add regression cases where appropriate.
4. Invite voluntary learner and contributor feedback, then publish anonymized findings with permission. No participants or outcomes are claimed in advance.
5. Expand number-line, vector and matrix examples once their correctness and accessible descriptions can be checked.

See [quality and open limitations](docs/quality-en.md) and the [community roadmap](docs/community-en.md). Claude subscription access would support interactive evaluation and maintenance. Separately billed API usage is not assumed to be included.
