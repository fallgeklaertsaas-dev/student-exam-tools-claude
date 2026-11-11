# Initial review notes / Erste Prüfnotizen

Date / Datum: 2026-11-11. Surface / Umgebung: Codex coding-assistant agents, not Claude / nicht Claude. Exact model version was not recorded / genaue Modellversion nicht erfasst. No claim of a complete automated behavioral benchmark / kein vollständiger automatischer Verhaltensbenchmark.

| DE forward-test task / Lernanfrage | Observed behavior / Beobachtetes Verhalten |
| --- | --- |
| Grade 5, only a hint for 3/4+1/6 / Klasse 5, nur Hinweis | Asked for equal-sized parts/common multiple without result / gleich große Teile und gemeinsames Vielfaches, kein Ergebnis |
| CD has at least two tracks, exact crow's foot / CD mit mindestens zwei Stücken | Explained (2,n) cannot be encoded exactly; reverse multiplicity unknown / Darstellungsgrenze und unbekannte Gegenrichtung genannt |
| All roots of z³=8i / alle Wurzeln | Three exact roots, explicit cubing checks / drei exakte Wurzeln mit Kubierproben |
| Namespace XML example / XML-Namensraumbeispiel | Elements have namespace, unprefixed id does not; no XSD claim / Elementnamensraum und namenraumloses id unterschieden; keine XSD-Zusage |
| Quadratic visual / Parabelgrafik | Executed bundled helper; produced SVG and inspected PNG; roots and vertex checked / Helfer ausgeführt, SVG erstellt, PNG geprüft; Nullstellen und Scheitel kontrolliert |

The reviewer independently ran the tests, checked portable ZIP metadata with a standard skill validator, built/installed an initial wheel in a temporary directory, and checked 1,200 random complex cases (reported maximum relative residual about 2.07e-14). It found decimal double-root, scientific-literal parsing and small-root scaling defects, now covered by regression tests. A conservative XML token rejection was documented as an intentional limit.

Die unabhängige Prüfung führte die Tests aus, prüfte ZIP-Metadaten mit einem Standard-Skillvalidator, baute/installierte ein anfängliches Wheel temporär und untersuchte 1.200 zufällige komplexe Fälle (gemeldete maximale relative Abweichung etwa 2,07e-14). Gefundene Fehler bei Dezimal-Doppelwurzeln, wissenschaftlicher Zahlenschreibweise und Skalierung kleiner Wurzeln sind durch Regressionstests abgesichert. Konservative XML-Textmarker-Ablehnung ist als bewusste Grenze dokumentiert.

This record summarizes observed trials; it does not replace raw with/without-skill Claude trials. Future trials should use result-template.json with full outputs and rubric results.

Dies fasst beobachtete Probeläufe zusammen und ersetzt keine Rohdaten aus Claude-Vergleichen mit/ohne Skill. Künftige Läufe sollen result-template.json mit vollständiger Ausgabe und Kriterienbewertung verwenden.
