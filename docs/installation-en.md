# Installation — English

[Deutsch](installation-de.md) · [Home](../README.md)

## Claude web / desktop

1. Review the skill instructions and bundled Python before enabling it. The original source is in `src/student_exam_tools/toolkit.py`.
2. From this repository's root run `python3 scripts/build_skills.py`. On Windows use `python` if necessary. You get one ZIP per locale in `dist/`.
3. In Claude, open the custom Skills area (currently Customize > Skills; navigation can change). Enable code execution if your account requires it and permits it. Follow the current [Anthropic creation guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
4. Upload **one** ZIP: English or German. Enable that skill. Do not upload the entire repository ZIP as a skill.
5. Start a new conversation and try a specific task, such as “Use Student Exam: only one hint for adding 3/4 and 1/6.” A response should stop before the answer.
6. For a tool smoke test, ask it to run the fraction helper for 3/4 and return an SVG. Inspect the generated file and confirm three of four equal cells are shaded. If execution is unavailable, expect source or text with that limitation stated.

Expected archive: `student-exam-en.zip` contains `student-exam-en/SKILL.md`, `student-exam-en/references/` and `student-exam-en/scripts/study_tools.py`. The DE archive uses the corresponding DE root. Skills do not grant paid subscriptions or circumvent account limits. Current plan availability is governed by Anthropic, not this repository.

## Claude Code — local project or personal use

Copy the complete folder, not only SKILL.md. In a terminal from the repository root:

```bash
mkdir -p .claude/skills
cp -R skills/student-exam-en .claude/skills/
```

For all local projects, copy instead to `~/.claude/skills/`. Do not overwrite an existing installation without reviewing differences. In Claude Code run `/student-exam-en` and state your task. To switch locale, remove the previously copied folder and install the other one; keep your own modified copy if needed. This repository does not perform installation automatically.

PowerShell equivalent (project scope):

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse skills/student-exam-en .claude/skills/
```

Local terminal instructions do not establish compatibility with every cloud or Cowork session. Follow the host-specific [official Skills documentation](https://code.claude.com/docs/en/skills).

## Standalone tools

Use Python 3.10 or newer. No `pip install` is needed:

```bash
python3 src/student_exam_tools/toolkit.py --help
python3 src/student_exam_tools/toolkit.py fraction 3 4 --output fraction.svg
python3 src/student_exam_tools/toolkit.py quadratic 1 -4 3 --analysis
python3 src/student_exam_tools/toolkit.py complex-roots 0 8 3 --analysis
```

Open SVG files in a browser or an SVG viewer. Mermaid requires a compatible renderer; GitHub can render fenced Mermaid in Markdown. The XML output is a text outline. The `.tex` worksheets require a separate LaTeX installation to compile.

## Troubleshooting and removal

| Symptom | Action |
| --- | --- |
| Skill not detected | Check folder/name/frontmatter and ZIP root; enable it in Claude |
| Both locales compete | Enable only one; request the other response language in chat |
| Python missing | Use an available trusted Python 3.10+ environment, or use text-only tutoring |
| Output already exists | Choose a new filename; the tool protects your old work |
| ER minimum of two rejected | Use explicit min–max notation; the helper intentionally cannot encode this |
| XML rejected | Check UTF-8, well-formedness, size and absence of DTD/entity declarations |
| Graph looks flat | Choose a more suitable x-window and inspect numeric axis scales |

Uninstall the account skill in Claude's Skills area, or remove the copied local skill folder. This does not delete your generated study files.
