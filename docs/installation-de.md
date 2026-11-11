# Installation — Deutsch

[English](installation-en.md) · [Start](../README.de.md)

## Claude im Web / Desktop

1. Lies Skill-Anweisungen und Python-Helfer vor dem Aktivieren. Der Originalcode liegt unter `src/student_exam_tools/toolkit.py`.
2. Führe im Hauptordner `python3 scripts/build_skills.py` aus. Unter Windows ist gegebenenfalls `python` der richtige Befehl. In `dist/` entsteht je ein ZIP pro Sprache.
3. Öffne in Claude den Bereich für eigene Skills (aktuell Customize > Skills; die Navigation kann sich ändern). Aktiviere bei Bedarf die Codeausführung, soweit dein Konto sie erlaubt. Beachte die aktuelle [Anthropic-Anleitung](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
4. Lade **ein** ZIP hoch: Deutsch oder Englisch. Aktiviere den Skill. Das gesamte Repository-ZIP ist kein installierbares Skill-Paket.
5. Beginne ein neues Gespräch, etwa mit „Nutze Student Exam: nur einen Hinweis zu 3/4 + 1/6“. Die Antwort sollte vor dem Ergebnis anhalten.
6. Bitte als Werkzeug-Kurztest um Ausführung des Bruchhelfers für 3/4 und um eine SVG-Datei. Prüfe drei markierte von vier gleich großen Zellen. Fehlt Ausführung, erwarte Quelltext oder Text mit einem klaren Hinweis auf diese Grenze.

Archivstruktur: `student-exam-de.zip` enthält `student-exam-de/SKILL.md`, `student-exam-de/references/` und `student-exam-de/scripts/study_tools.py`. Das englische ZIP nutzt den entsprechenden EN-Hauptordner. Skills schalten kein Bezahlabo frei und umgehen keine Kontolimits. Die aktuelle Verfügbarkeit der Funktionen legt Anthropic fest.

## Claude Code — lokales Projekt oder persönliche Nutzung

Kopiere den vollständigen Ordner, nicht nur SKILL.md. Im Terminal im Hauptordner:

```bash
mkdir -p .claude/skills
cp -R skills/student-exam-de .claude/skills/
```

Kopiere für alle lokalen Projekte stattdessen nach `~/.claude/skills/`. Überschreibe eine bestehende Installation erst nach Vergleich der Änderungen. Starte in Claude Code `/student-exam-de` und nenne deine Aufgabe. Entferne beim Sprachwechsel den zuvor kopierten Ordner und installiere den anderen; sichere eigene Änderungen bei Bedarf. Dieses Repository installiert nichts automatisch.

PowerShell-Variante (Projektumfang):

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse skills/student-exam-de .claude/skills/
```

Diese lokale Terminal-Anleitung bestätigt keine Kompatibilität mit jeder Cloud- oder Cowork-Sitzung. Nutze die zur Umgebung passende [offizielle Skill-Dokumentation](https://code.claude.com/docs/en/skills).

## Werkzeuge ohne Claude

Python 3.10 oder neuer. Kein `pip install` nötig:

```bash
python3 src/student_exam_tools/toolkit.py --help
python3 src/student_exam_tools/toolkit.py fraction 3 4 --lang de --output bruch.svg
python3 src/student_exam_tools/toolkit.py quadratic 1 -4 3 --analysis
python3 src/student_exam_tools/toolkit.py complex-roots 0 8 3 --analysis
```

Öffne SVG-Dateien im Browser oder SVG-Betrachter. Mermaid benötigt einen geeigneten Renderer; GitHub stellt Mermaid-Codeblöcke in Markdown dar. Die XML-Ausgabe ist eine Textübersicht. Die `.tex`-Arbeitsblätter benötigen zum Kompilieren ein separates LaTeX-System.

## Fehlerbehebung und Entfernen

| Problem | Maßnahme |
| --- | --- |
| Skill wird nicht erkannt | Ordner, Name, Frontmatter und ZIP-Hauptordner prüfen; in Claude aktivieren |
| Beide Sprachen konkurrieren | Nur einen Skill aktivieren; andere Antwortsprache im Chat anfordern |
| Python fehlt | Vertrauenswürdige Python-3.10+-Umgebung nutzen oder in Textform lernen |
| Ausgabedatei existiert bereits | Neuen Namen wählen; das Werkzeug schützt alte Arbeit |
| ER-Minimum zwei wird abgelehnt | Ausdrückliche Min–Max-Notation wählen; der Helfer kann dies bewusst nicht ausdrücken |
| XML wird abgelehnt | UTF-8, Wohlgeformtheit, Größe und fehlende DTD-/Entity-Deklarationen prüfen |
| Graph wirkt flach | Geeigneteren x-Ausschnitt wählen und numerische Achsenskalen beachten |

Entferne den Konto-Skill in Claudes Skill-Bereich oder den lokal kopierten Skill-Ordner. Deine erzeugten Lerndateien bleiben erhalten.
