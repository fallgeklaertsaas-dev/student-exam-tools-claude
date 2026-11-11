# Entwurfsquellen — Deutsch

[English](sources-en.md)

Offizielle Primärquellen, geprüft am **11.11.2026**. Sie begründen Entwurfsentscheidungen, keine Empfehlung durch Anthropic. Skill-Anweisungen, Werkzeuge und Aufgaben sind eigene Inhalte; fremde Dokumentation wird kurz zusammengefasst statt übernommen.

| Offizielle Quelle | Umsetzung in diesem Projekt |
| --- | --- |
| [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) | Eine kurze Einstiegsdatei verweist auf Referenzen und optionale Skripte; nur das benötigte Thema wird geladen. |
| [Claude Platform: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Wiederverwendbare Anweisungen werden von Einzelprompts getrennt und mit Ressourcen als Skill-Ordner gebündelt. |
| [Claude Platform: authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Kurze Anweisungen, konkrete Beschreibungen und aufgabenbezogene Tests; ein Evaluationssatz begleitet die Umsetzung. |
| [Claude Code: extend Claude with skills](https://code.claude.com/docs/en/skills) | Lokale Projekt-/Benutzerpfade und direkte Slash-Aufrufe werden getrennt vom Konto-Upload erklärt. |
| [Claude Help: create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) | Name/Beschreibung und ein zum Skill passender Hauptordner je ZIP; Installation und echte Aufgaben prüfen. Beschreibungen bleiben für Kompatibilität unter 200 Zeichen. |
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Testfälle, beobachtete Ausgaben und Bewertung unterscheiden; offenlegen, dass Codetests keine Live-Modell-Evaluation sind. |
| [Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) | Qualität allein begründet keine Teilnahmeberechtigung; reale Nutzung und Beiträge dokumentieren statt Qualifikation zu behaupten. |

Zusätzliche Implementierungsquelle: [Mermaid-ER-Parser](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/diagrams/er/parser/erDiagram.jison), geprüft auf Endpunktsyntax und reservierte Marker. Daraus folgt keine Kompatibilität mit jeder Renderer-Version.

Die Lernregeln (zunächst Hinweise, exakte Algebra-Proben, offene Kardinalitäten und niveaugerechte Erklärung) sind eigene Entwurfsentscheidungen. Daraus folgt keine wissenschaftlich belegte Verbesserung von Noten.

Installationsmenüs und Programmschwellen können sich ändern. Die offiziellen Seiten haben Vorrang vor dieser Momentaufnahme. Das Projekt übernimmt weder Anthropic-Markenzeichen noch ein angebliches offizielles Zertifikat.
