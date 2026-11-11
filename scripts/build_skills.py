"""Sync portable standard-library helpers and build deterministic upload ZIPs."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build(check=False):
    canonical = (ROOT / "src/student_exam_tools/toolkit.py").read_bytes()
    for locale in ("en", "de"):
        folder = ROOT / f"skills/student-exam-{locale}"
        target = folder / "scripts/study_tools.py"
        license_target = folder / "LICENSE.txt"
        license_content = (ROOT / "LICENSE").read_bytes()
        if check:
            if not license_target.exists() or license_target.read_bytes() != license_content:
                raise SystemExit(f"Out-of-date license: {license_target}")
            if not target.exists() or target.read_bytes() != canonical:
                raise SystemExit(f"Out-of-date helper: {target}")
        else:
            target.write_bytes(canonical)
            license_target.write_bytes(license_content)
    if check:
        print("Portable helpers match canonical source.")
        return
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    hashes = {}
    for locale in ("en", "de"):
        folder = ROOT / f"skills/student-exam-{locale}"
        archive = dist / f"{folder.name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
            for path in sorted(folder.rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts:
                    info = zipfile.ZipInfo(path.relative_to(folder.parent).as_posix(), (2026, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    output.writestr(info, path.read_bytes())
        hashes[archive.name] = hashlib.sha256(archive.read_bytes()).hexdigest()
    (dist / "SHA256SUMS.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print(json.dumps(hashes, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    build(parser.parse_args().check)
