# Projektfakten und Nachweise

[English](PROJECT.md) · [README](README.de.md) · [Strukturierte Fakten](project.json)

Student Exam Tools for Claude ist ein studentisch entwickeltes Projekt unter MIT-Lizenz. Es bündelt einen visuellen Lernablauf in zwei installierbaren Agent Skills und fünf lokalen Python-Helfern. Die frühe öffentliche Version wird unter [fallgeklaertsaas-dev/student-exam-tools-claude](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude) gepflegt.

## Welches Problem es bearbeitet

Beim Übergang von Schulmathematik zu einführender Uni-Mathematik und Informationsmodellierung benötigen Lernende unterschiedliche Darstellungen ihrer Denkwege: gleich große Bruchteile, beschriftete Funktionsgraphen, die komplexe Ebene, ausdrückliche Beziehungskardinalitäten und XML-Hierarchien. Das Projekt verbindet diese Darstellungen in einem wiederverwendbaren deutschen und englischen Lernablauf mit Hinweis-, Kontroll- und Übungsmodi.

Der angestrebte Beitrag sind nachvollziehbare Denkwege und wiederverwendbare Lernmaterialien. Eine Verbesserung von Noten oder eine von keinem anderen Werkzeug bearbeitete Marktlücke wurde nicht nachgewiesen.

## Was sich jetzt überprüfen lässt

| Fakt | Nachweis |
| --- | --- |
| Zwei Sprachpakete | [Deutscher Skill](skills/student-exam-de/SKILL.md), [englischer Skill](skills/student-exam-en/SKILL.md), [Upload-Pakete](packages) |
| Fünf ausführbare Helfer | [Python-Originalcode](src/student_exam_tools/toolkit.py): fraction, quadratic, complex-roots, er, xml |
| Lokale Ausführung ohne API-Schlüssel | Implementierung mit Standardbibliothek; [Installationsanleitung](docs/installation-de.md) |
| 54 automatische Testmethoden | [Testcode](tests/test_toolkit.py), [bestandener GitHub-Lauf](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude/actions/runs/42990301301) |
| Prüfungen unter Python 3.10, 3.12 und 3.13 | [CI-Workflow](.github/workflows/ci.yml), verlinkter bestandener Lauf |
| 20 zweisprachige Verhaltensfälle definiert | [Falldefinitionen](evals/cases.json); der vollständige Claude-Vergleich wurde nicht ausgeführt |
| Öffentliche visuelle Beispiele | [Deutsche/englische Bilder](docs/images), [durchgerechnete Beispiele](docs/examples-de.md) |
| Lizenz und Beitragsprozess | [MIT-Lizenz](LICENSE), [Mitwirkungsanleitung](CONTRIBUTING.de.md), [Issue-Vorlagen](.github/ISSUE_TEMPLATE) |

Codetests, erzeugte Bilder und definierte Evaluationsfälle sind unterschiedliche Nachweise. Keiner davon misst tatsächliche Nutzung oder Lernergebnisse.

## Momentaufnahme der öffentlichen Reichweite

Beobachtet am **12.11.2026** über die öffentlichen GitHub-Endpunkte für Repository, Mitwirkende, Pull Requests und Releases. Dies sind datierte Werte, keine Live-Analyse.

| Kennzahl | Beobachteter Wert |
| --- | --- |
| Repository erstellt | 11.11.2026 |
| Sterne / Forks | 0 / 0 |
| Gelistete Mitwirkende | 1, das Maintainer-Konto |
| Beobachtete externe Mitwirkende | 0 |
| Zusammengeführte Pull Requests | 0 |
| Veröffentlichte GitHub-Releases | 0; Skill-ZIPs liegen als Repository-Dateien vor |
| Eindeutige Downloads oder aktive Nutzende | Nicht gemessen |
| Nachgewiesene abhängige Projekte oder institutionelle Nutzung | Nicht dokumentiert |

Die Quellendpunkte stehen in [project.json](project.json). Downloadzahlen von Release-Anhängen sind kein Ersatz für direkte ZIP-Downloads aus Repository-Dateien. Fehlende Nutzungsnachweise messen nicht jede möglicherweise stattgefundene Verwendung.

## Nächste Arbeit mit überprüfbaren Ergebnissen

1. Beide Sprachpakete in Claude installieren und testen; Modell, Umgebung, Prompts, Ausgaben und Fehler genau erfassen.
2. Die 20 Fälle in beiden Sprachen, jeweils mit und ohne Skill, in drei Versuchen je Bedingung bearbeiten: Ziel sind 240 protokollierte Gesprächsversuche. Dies sind geplante Versuche, keine erledigten Tests oder Nutzerzahlen.
3. Erklärungen und Darstellungen anhand protokollierter Fehler verbessern und passende Regressionstests ergänzen.
4. Freiwillige Rückmeldungen von Lernenden und Mitwirkenden einholen; anonymisierte Ergebnisse mit Erlaubnis veröffentlichen. Teilnehmende oder Ergebnisse werden nicht vorweggenommen.
5. Beispiele für Zahlengeraden, Vektoren und Matrizen ausbauen, sobald Fachlichkeit und zugängliche Beschreibungen überprüfbar sind.

Siehe [Qualität und offene Grenzen](docs/quality-de.md) und den [Community-Entwicklungsplan](docs/community-de.md). Ein Claude-Abonnement würde interaktive Evaluation und Pflege unterstützen. Separat abgerechnete API-Nutzung wird dabei nicht als enthalten vorausgesetzt.
