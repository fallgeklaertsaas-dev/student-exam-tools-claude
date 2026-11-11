# Maintainer instructions / Hinweise für Bearbeitungen

- Canonical tool code / Originalwerkzeug: `src/student_exam_tools/toolkit.py`.
- Regenerate portable copies and ZIPs with / Kopien und ZIPs erzeugen: `python3 scripts/build_skills.py`.
- Validate meaningful changes with / Fachliche Änderungen prüfen: `python3 -m unittest discover -s tests -v` and/und `python3 scripts/validate_repo.py`.
- Keep EN/DE features aligned; note unverified translations / Sprachfunktionen gleichwertig halten; ungeprüfte Übersetzungen kennzeichnen.
- Add behavioral cases for instruction changes / Bei Anweisungsänderungen Verhaltensfälle ergänzen: `evals/cases.json`.
- Preserve hint-mode boundaries and explicit cardinality evidence / Hinweisgrenzen und Kardinalitätsbelege erhalten.
- Do not add credentials, telemetry or unrequested network calls / Keine Zugangsdaten, Telemetrie oder unnötigen Netzwerkaufrufe ergänzen.
- Report only actual checks and real adoption; no qualification guarantees / Nur echte Prüfungen und Nutzung nennen; keine Aufnahmegarantien.
