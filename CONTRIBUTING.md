# Contributing

[Deutsch](CONTRIBUTING.de.md)

Start with a reproducible small improvement: a clearer hint, a counterexample, a verified translation, an accessibility improvement or a failing test for a real bug. No contribution quota is imposed.

1. Open an issue describing the problem, learner level, expected behavior and observed behavior. Use original or openly licensed sample tasks. Remove names, grades, student IDs, tokens and private course material.
2. Make one focused change on your branch. If tool behavior changes, add a test that would catch the error. If a skill instruction changes, add or update a behavioral case in `evals/cases.json`.
3. Keep EN/DE behavior aligned. You may submit in either language; explicitly flag any counterpart still needing translation.
4. Run `python3 scripts/build_skills.py` after changing canonical toolkit code; do not edit the two generated script copies directly. Run tests and repository validation.
5. Describe what changed, why, and the checks you actually ran. Label unexecuted checks. A human maintainer reviews correctness and language before merging.

For model trials, use the same prompt with and without the skill in fresh conversations. Record model ID/version, date, host, mode, tool access, output and rubric scores; use several trials and retain failures. Never call an unrun evaluation a pass. See [quality](docs/quality-en.md).

AI-assisted contributions are welcome. Disclose substantial AI assistance and verify outputs. Authors remain responsible for licensing and accuracy. Do not contribute copied textbooks, exam dumps, secrets or unauthorized personal data. Contributions are licensed under the repository's MIT license; do not submit work you cannot license.

Do not create fake users, manufactured PRs, irrelevant contributions, reciprocal star campaigns or fabricated adoption numbers. Useful work and honest evaluation matter more than volume.
