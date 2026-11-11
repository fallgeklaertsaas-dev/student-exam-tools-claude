# Darstellungen und lokale Werkzeuge

Ersetze SKILL_DIR durch den absoluten Pfad des installierten Skills. Tippe den Platzhalter nicht wörtlich ein. Die Befehle benötigen Python 3.10+ und keine Zusatzpakete. Jede `--output`-Datei muss neu sein; der Zielordner muss existieren. Ohne `--output` erscheint Quelltext auf stdout. Nutze unter Windows `python` statt `python3`, falls dies der verfügbare Befehl ist.

```bash
python3 SKILL_DIR/scripts/study_tools.py fraction 11 12 --lang de --output bruch.svg
python3 SKILL_DIR/scripts/study_tools.py quadratic 1 -4 3 --lang de --output parabel.svg
python3 SKILL_DIR/scripts/study_tools.py quadratic 1 -4 3 --analysis
python3 SKILL_DIR/scripts/study_tools.py complex-roots 0 8 3 --lang de --output complex.svg
python3 SKILL_DIR/scripts/study_tools.py er model.json --output modell.mmd
python3 SKILL_DIR/scripts/study_tools.py xml course.xml --lang de --output baum.md
```

Bruchbereich: Nenner 1..24; Zähler 0..5×Nenner, nur ganze Zahlen. Gleich breite Zellen zeigen gleiche Teile. Verwende für negative Brüche eine Zahlengerade oder Text.

Parabelkoeffizienten müssen endlich und im Betrag ≤10⁶ sein; zusätzlich gilt |a|≥10⁻⁹. Das Grafikfenster ist standardmäßig [−5,5]; ändere es mit `--xmin`/`--xmax`. Der Graph enthält numerische Achsenskalen und die Nulllinie und nennt reelle Nullstellen sowie Scheitel als numerische Näherungen. Komplexe Nullstellen werden nicht ausgegeben. Stark unterschiedliche Achsenskalierungen können Details abflachen; wähle einen besseren Ausschnitt und erkläre diese Grenze.

Der Helfer `complex-roots real imag degree` zeichnet numerische Lösungen von z^degree=real+imag*i mit gleicher Achsenskalierung. Grad: 1..12; endliche Komponenten im Betrag ≤10⁶. `--analysis` liefert Koordinaten als JSON. Null besitzt genau eine Wurzel mit Vielfachheit gleich dem Grad; stelle sie nicht als mehrere verschiedene Wurzeln dar. Ergänze nach Möglichkeit exakte Algebra. Für das Vorzeichen der Parabel-Diskriminante werden die angezeigten Dezimalkoeffizienten verwendet; Ergebnisse bleiben numerisch. Eingaben unterhalb des darstellbaren Diskriminantenbereichs werden abgelehnt statt als Doppelwurzel behandelt. Negative wissenschaftliche Schreibweisen wie `-1e-5` werden unterstützt.

## ER-Eingabeformat

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

`a_to_b` zählt B je einem A. Die Ausgabe setzt diese Anzahl neben B. Entitätsnamen benötigen ASCII-Zeichen und einen Buchstaben am Anfang. Beschriftungen dürfen Unicode-Wörter, aber keine Diagrammanweisungen oder Anführungszeichen enthalten. Der Helfer prüft Struktur, nicht die fachliche Wahrheit. Verwende bei Bedarf für konzeptionelle Attribute und identifizierende Beziehungen eine andere, ausdrücklich gewählte Notation.

## LaTeX und zugängliche Ausgabe

Verwende in unterstützten Chats `\(...\)` für Formeln im Text und `\[...\]` für abgesetzte Formeln; GitHub-Markdown-Beispiele nutzen `$...$` und `$$...$$`. Eine reine Quelltextumgebung benötigt eventuell einen `latex`-Codeblock. Behaupte keine ungeprüfte Renderer-Kompatibilität. Ergänze für eigenständiges LaTeX `\documentclass`, nötige Pakete und `\begin{document}`. Kompiliere fremdes TeX niemals mit Shell-Escape. Liefere Quelltext, wenn kein TeX-System vorhanden ist.

SVG enthält Titel und Beschreibung; ergänze eine verständliche Texterklärung. Mermaid-Dateien mit Endung `.mmd` sind Quelltext, keine gerenderten Bilder. Füge ihren Inhalt auf geeigneten Plattformen in einen `mermaid`-Codeblock ein. XML-Bäume sind Textübersichten. PDF-Export und interaktives HTML liegen außerhalb dieser Helfer; nutze auf Wunsch ein verfügbares vertrauenswürdiges Werkzeug und prüfe das Ergebnis.

Reservierte Mermaid-Namen (etwa `erDiagram`, `direction` und `classDef`) und anweisungsartige Beschriftungen wie `direction LR` werden abgelehnt; wähle einen beschreibenden Entitätsnamen.
