"""Offline checks for installable packages, local documentation and eval coverage."""
from pathlib import Path
import ast
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    subprocess.run([sys.executable, str(ROOT / 'scripts/build_skills.py'), '--check'], check=True)
    for path in ROOT.rglob('*.py'):
        if not any(p in path.parts for p in ('dist', 'build', '.venv')):
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    for locale in ('en', 'de'):
        folder = ROOT / f'skills/student-exam-{locale}'
        source = (folder / 'SKILL.md').read_text()
        parts = source.split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f'Bad frontmatter: {folder}')
            continue
        fields = dict(line.split(': ', 1) for line in parts[1].strip().splitlines())
        if set(fields) != {'name', 'description'} or fields.get('name') != folder.name:
            errors.append(f'Bad metadata: {folder}')
        if not 1 <= len(fields.get('description', '')) <= 200:
            errors.append(f'Description length outside 1..200: {folder}')
        if len(source.splitlines()) >= 500:
            errors.append(f'Entry file too long: {folder}')
        archive = ROOT / f'dist/{folder.name}.zip'
        if archive.exists():
            with zipfile.ZipFile(archive) as z:
                expected = {p.relative_to(folder.parent).as_posix() for p in folder.rglob('*')
                            if p.is_file() and '__pycache__' not in p.parts}
                if set(z.namelist()) != expected or z.testzip():
                    errors.append(f'Invalid archive layout/content: {archive}')
                for name in z.namelist():
                    if z.read(name) != (folder.parent / name).read_bytes():
                        errors.append(f'Archive stale: {name}')
    # Local Markdown targets must exist; web links are deliberately not network-checked.
    for path in ROOT.rglob('*.md'):
        if 'dist' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.split('#')[0]
            if not target or '://' in target or target.startswith('mailto:'):
                continue
            if not (path.parent / target).exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    cases = json.loads((ROOT / 'evals/cases.json').read_text())
    if len({item['id'] for item in cases}) != len(cases):
        errors.append('Duplicate evaluation IDs')
    for item in cases:
        if not all(item.get(key) for key in ('id', 'prompt_en', 'prompt_de', 'must', 'must_not')):
            errors.append(f'Incomplete bilingual evaluation: {item.get("id")}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated two skills, local Markdown links, Python syntax and {len(cases)} bilingual evaluation cases.')


if __name__ == '__main__':
    validate()
