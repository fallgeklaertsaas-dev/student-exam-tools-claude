# Visuelle GitHub-Vorschau

[English](visuals-en.md) · [Start](../README.de.md)

Die README nutzt PNG-Dateien, damit GitHub sie direkt zeigt und Besuchende weder einen Skill ausführen noch einen Diagrammeditor öffnen müssen. Jedes Bild hat in der README einen Alternativtext und einen Bezug zu den dokumentierten Beispielen.

| Vorschau | Tatsächliche Quelle und Bedeutung |
| --- | --- |
| Bruch | SVG des Originalhelfers zu 11/12: elf markierte Teile eines Ganzen, insgesamt zwölf gleich große Teile |
| Parabel | SVG des Originalhelfers zu x²−4x+3: Nullstellen 1 und 3, Scheitel (2,−1); numerischer Graph mit Achsenskalen |
| Komplexe Wurzeln | SVG des Originalhelfers zu z³=8i: drei Wurzeln auf einem Kreis mit Radius 2 bei gleicher Achsenskalierung |
| ER | Graphviz-Zeichnung der Beziehungen aus examples/enrollment.json; die Beschriftung zählt Instanzen am jeweiligen Ende; der Helfer selbst erzeugt Mermaid-Quelltext |
| XML | Unveränderter Baumtext aus examples/xml-de.md in lesbarer Bildform; ohne Elementtexte oder Attributwerte |
| Formeln | Mit Matplotlib MathText dargestellte Formeln der eigenen Beispiele; kein Screenshot eines kompilierten LaTeX-Arbeitsblatts |
| Übersicht | Zusammenstellung der sechs Vorschauen mit Projekttitel und studentischem Motto |

Kein Vorschaubild wird als Screenshot von Claude oder einer interaktiven Anwendung ausgegeben. Funktionsgraphen sind numerische Ansichten; exakte Begründungen stehen in den Beispielen. Die ER-Zeichnung nennt Annahmen, statt Kursvorgaben zu erfinden. Vollständige PNGs und ursprüngliche SVG-/XML-/JSON-/TeX-Quellen liegen bei.

## Bilder neu erzeugen

Optionale Dokumentationsabhängigkeiten: Python mit Pillow und Matplotlib sowie Inkscape und Graphviz (`dot`) im PATH. Dies sind **keine Laufzeitanforderungen** der installierten Skills oder Lernwerkzeuge. Das Skript verwendet nach Möglichkeit DejaVu-Sans-Schriften.

Im Hauptordner ausführen:

```bash
python3 scripts/build_previews.py
```

Dadurch entstehen alle 14 deutschen und englischen PNGs unter docs/images aus beiliegenden Beispielen und Beschriftungen neu. Prüfe bei Änderungen der Beispieldaten auch Diagrammbeziehungen und Bildtexte. Kontrolliere die neuen Bilder visuell und führe vor dem Commit `python3 scripts/validate_repo.py` aus, um lokale Bildlinks zu prüfen.
