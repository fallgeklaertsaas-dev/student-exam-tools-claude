# Design sources — English

[Deutsch](sources-de.md)

Official primary sources reviewed on **2026-11-11**. These are design references, not evidence of endorsement. All skill instructions, tools and exercises in this repository are original; documentation is summarized briefly, not reproduced.

| Official source | How it informed this project |
| --- | --- |
| [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) | A small entry file routes to references and optional scripts; load only the relevant topic. |
| [Claude Platform: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Separate reusable instructions from a one-off prompt; package the resources as a skill directory. |
| [Claude Platform: authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Keep instructions concise, descriptions specific and tests task-oriented. An evaluation set accompanies the implementation. |
| [Claude Code: extend Claude with skills](https://code.claude.com/docs/en/skills) | Document local project/personal paths and direct slash invocation separately from account upload. |
| [Claude Help: create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) | Include name/description and a single matching skill root in each ZIP; test installation and actual tasks. Descriptions are kept below 200 characters for compatibility. |
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Distinguish test cases, observable outputs and grading; disclose that code tests are not live-model evaluations. |
| [Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) | Quality alone does not establish eligibility; document real adoption and contributions instead of claiming qualification. |

Additional implementation reference: [Mermaid ER parser](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/diagrams/er/parser/erDiagram.jison), reviewed for endpoint syntax and reserved tokens. This does not establish compatibility with every renderer version.

The lesson design (hint-first defaults, exact algebra checks, uncertainty in cardinalities and age-appropriate explanation) is the project's own implementation judgment. This is not a research claim that these workflows improve grades.

Installation menus and program thresholds can change. The linked official pages take precedence over a frozen copy of this documentation. There is no copied Anthropic branding or official certification badge.
