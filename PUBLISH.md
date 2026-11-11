# Publish the prepared repository / Vorbereitetes Repository veröffentlichen

**EN:** This source archive is ready for a new, separate GitHub repository named `student-exam-tools-claude`. Do not copy it into an unrelated existing repository. Keep the source repository and the two installable skill ZIPs distinct.

**DE:** Dieses Quellarchiv ist für ein neues, separates GitHub-Repository namens `student-exam-tools-claude` vorbereitet. Kopiere es nicht in ein sachfremdes bestehendes Repository. Unterscheide Quellrepository und die beiden installierbaren Skill-ZIPs.

## Connected repository / Verbundenes Repository

Repository: [fallgeklaertsaas-dev/student-exam-tools-claude](https://github.com/fallgeklaertsaas-dev/student-exam-tools-claude)

**EN:** This is the selected public repository. Review changes before updating it; do not create a duplicate repository or copy these files into another project. Remote CI and account installation are separate verification steps.

**DE:** Dies ist das gewählte öffentliche Repository. Prüfe Änderungen vor Aktualisierungen; erstelle kein doppeltes Repository und kopiere die Dateien nicht in ein anderes Projekt. Remote-CI und Konto-Installation sind getrennte Prüfschritte.

## Local publication workflow / Lokaler Veröffentlichungsablauf

After extracting the source archive, from its root / Nach Entpacken im Hauptordner:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_skills.py
python3 scripts/validate_repo.py

git init -b main
git add .
git commit -m "Add bilingual visual study skills and offline tools"
gh auth login
gh repo create student-exam-tools-claude --public --source=. --remote=origin --push
```

**EN:** Set your own local Git author identity if Git requests it. Review the repository visibility and account before publishing. If the repository already exists, do not repeat `gh repo create`; use its verified URL as your remote instead. Upload the two `dist/student-exam-*.zip` files and `dist/SHA256SUMS.json` as release assets only after reviewing the CI results. Do not call an unexecuted remote workflow a pass.

**DE:** Setze bei Bedarf deine lokale Git-Autorenidentität. Prüfe Konto und öffentliche Sichtbarkeit vor Veröffentlichung. Existiert das Repository bereits, wiederhole `gh repo create` nicht, sondern nutze seine geprüfte URL als Remote. Lade die beiden `dist/student-exam-*.zip`-Dateien und `dist/SHA256SUMS.json` erst nach Prüfung der CI-Ergebnisse als Release-Anhänge hoch. Behaupte keinen bestandenen Remote-Workflow ohne dessen Ausführung.
