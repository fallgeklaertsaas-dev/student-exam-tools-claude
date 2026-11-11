# Mitwirken

[English](CONTRIBUTING.md)

Beginne mit einer kleinen, nachvollziehbaren Verbesserung: verständlicherer Hinweis, Gegenbeispiel, geprüfte Übersetzung, bessere Zugänglichkeit oder ein Fehlertest für einen echten Bug. Es gibt keine Beitragsquote.

1. Beschreibe im Issue Problem, Lernniveau, erwartetes und beobachtetes Verhalten. Nutze eigene oder offen lizenzierte Beispielaufgaben. Entferne Namen, personenbezogene Noten, Matrikelnummern, Tokens und private Kursunterlagen.
2. Bearbeite eine klar begrenzte Änderung auf deinem Branch. Ergänze bei geändertem Werkzeugverhalten einen Test, der den Fehler erkennt. Ergänze bei Skill-Änderungen einen Verhaltensfall in `evals/cases.json`.
3. Halte deutsches und englisches Verhalten gleichwertig. Beiträge sind in beiden Sprachen möglich; kennzeichne eine noch offene Übersetzung ausdrücklich.
4. Führe nach Änderungen am Originalwerkzeug `python3 scripts/build_skills.py` aus; bearbeite die beiden erzeugten Skriptkopien nicht direkt. Führe Tests und Repository-Prüfung aus.
5. Erkläre Änderung, Grund und tatsächlich ausgeführte Prüfungen. Kennzeichne nicht ausgeführte Prüfungen. Ein menschlicher Maintainer prüft Fachlichkeit und Sprache vor dem Zusammenführen.

Nutze für Modellversuche denselben Prompt mit und ohne Skill in frischen Gesprächen. Erfasse Modell-ID/Version, Datum, Umgebung, Modus, Werkzeugzugriff, Ausgabe und Kriterienbewertung. Führe mehrere Versuche aus und erhalte auch Fehlschläge. Eine nicht durchgeführte Evaluation ist kein bestandener Test. Siehe [Qualität](docs/quality-de.md).

KI-unterstützte Beiträge sind willkommen. Lege wesentliche KI-Hilfe offen und überprüfe Ergebnisse. Autorinnen und Autoren bleiben für Lizenz und Richtigkeit verantwortlich. Keine kopierten Lehrbücher, Prüfungssammlungen, Geheimnisse oder unzulässigen personenbezogenen Daten. Beiträge stehen unter der MIT-Lizenz des Projekts; reiche nur Inhalte ein, die du so lizenzieren darfst.

Keine Scheinaccounts, künstlichen PRs, sachfremden Beiträge, gegenseitigen Sternkampagnen oder erfundenen Nutzungszahlen. Nützliche Arbeit und ehrliche Prüfung zählen mehr als Menge.
