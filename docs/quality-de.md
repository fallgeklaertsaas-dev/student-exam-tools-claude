# Prüfung und Grenzen — Deutsch

[English](quality-en.md) · [Start](../README.de.md)

Geprüft am **11.11.2026** mit Python **3.12.14**. Dieser Nachweis nennt tatsächliche Prüfungen; er verspricht weder Perfektion noch bessere Prüfungsergebnisse.

## Drei Prüfdurchgänge

| Durchgang | Tatsächliche Prüfungen | Ergebnis / Änderungen |
| --- | --- | --- |
| 1. Technik und Pakete | Unit- und variierende Testfälle ausgeführt; beide portablen Skripte außerhalb des Repositories gestartet; deterministische ZIPs gebaut; Pfade, Python-Syntax, Metadaten, Verlinkungen und Skriptgleichheit geprüft | Alle 54 Testmethoden bestanden, darunter 150 reproduzierbare Parabelfälle und alle 16 Endpunktkombinationen. Installierbare ZIPs besitzen genau einen passenden Hauptordner und die MIT-Lizenz. |
| 2. Fachlichkeit, Sprachen und Fehlereingaben | Beispiele an Ausgangsgleichungen geprüft; deutsche/englische Regeln und Dokumentationszusagen verglichen; unabhängige Prüfung von Zahlen-/CLI-Randfällen und temporärer Wheel-Installation | Dezimal-Doppelwurzel-Erkennung und negative wissenschaftliche Schreibweise korrigiert und mit Regressionstests abgesichert. Skalierung kleiner komplexer Wurzeln korrigiert. Konservative XML-Ablehnung von Deklarationsmarkern in Kommentaren/CDATA dokumentiert und getestet. |
| 3. Lernablauf und Sichtprüfung | Separater Agent bearbeitete fünf Lernanfragen mit dem deutschen Skill; SVGs erzeugt und gerendert geprüft; Hinweisgrenzen, ER-Unklarheiten, komplexe Wurzeln und Namensräume untersucht | Hinweis verriet kein Ergebnis; (2,n) wurde nicht abgeschwächt; Kubikwurzeln enthielten Proben; XML-Namensräume wurden unterschieden. Bruch-, Parabel- und komplexe Wurzelbeispiele wurden mit Inkscape gerendert und visuell geprüft. |

Der Fünf-Aufgaben-Lauf verwendete einen anderen Programmierassistenten, **nicht Claude**. Er ist ein kleiner qualitativer Probelauf, keine repräsentative Studie und kein Live-Claude-Benchmark. Die unabhängige Prüfung umfasste zusätzlich 1.200 zufällige komplexe Wurzelfälle mit kleinen Abweichungen bei der Probe in der Ausgangsgleichung. Das ist eine numerische Kontrolle, kein Beweis sämtlicher Gleitkommafälle. Siehe [Prüfnotizen](../evals/review-notes.md).

## Automatische Prüfungen wiederholen

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_skills.py
python3 scripts/validate_repo.py
```

Führe `build_skills.py` zweimal aus und vergleiche `dist/SHA256SUMS.json` auf deterministische Ausgabe. Beide Sprachpakete enthalten identische Python-Originalbytes; Anweisungen und Referenztexte sind übersetzt. Im Review wurde ein Wheel des geprüften Quellstands in ein isoliertes temporäres Ziel gebaut und installiert. Eine Veröffentlichung auf PyPI wird damit nicht behauptet.

## Noch nicht verifiziert

- Installation und tatsächliches Modellverhalten in Claude Web/Desktop und lokalem Claude Code. Es gab keine Claude-Kontositzung und keinen API-Schlüssel. Die 20 zweisprachigen Verhaltensfälle sind definiert; die vollständige Claude-Evaluation mit/ohne Skill wurde **nicht ausgeführt**.
- CI-Ausführung unter Python 3.10 und 3.13. Der Workflow ist vorbereitet; vor Veröffentlichung wird kein GitHub-Prüflauf behauptet. Lokal lief Python 3.12.14.
- TeX-Kompilierung: Beide Arbeitsblattversuche scheiterten am fehlenden `pdflatex.fmt` dieser Umgebung. Die `.tex`-Dateien sind Quellen, keine verifizierten PDFs.
- Mermaid-Darstellung in verschiedenen Umgebungsversionen. Syntax und Kardinalitätszuordnung sind geprüft; ein gerenderter Mermaid-Release-Screenshot liegt nicht vor.
- Lernwirksamkeit, sämtliche Schullehrpläne, beliebige mathematische Terme, allgemeine symbolische Integration, XSD-Validierung, identifizierende/ternäre ER-Beziehungen und alle Kombinationen assistiver Technik.

## Protokoll für Verhaltensevaluation

Nutze `evals/cases.json` und kopiere `evals/result-template.json` je Versuch. Vergleiche für jede Sprache ein frisches Gespräch mit aktiviertem Skill mit demselben Prompt ohne Skill. Erfasse Umgebung, Modell/Version, Datum, Werkzeugrechte und die vollständige beobachtbare Antwort. Führe vor Schlussfolgerungen mindestens drei Versuche je Bedingung aus und erhalte Fehler. Bewerte jedes `must`-/`must_not`-Kriterium ausdrücklich statt nur den Stil. Erfinde keine fehlenden Daten und leite Modellleistung nicht aus Codetests ab.

Veröffentliche anonymisierte Ergebnisse mit klaren Grenzen und nötiger Erlaubnis. Unverständliche Hinweise, falsche Kardinalitäten und unbelegte Richtigkeitszusagen sind auch bei bestandenen Codetests Fehler.
