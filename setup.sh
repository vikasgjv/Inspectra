
#!/bin/bash
set -e

echo "Downloading Inspectra model artifacts..."

DRIVE_URL="https://drive.google.com/drive/folders/1ONjK_OWgHW22AoR_WLqBSyhd7sQzs6h8"

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL_DIR="$ROOT_DIR/backend/models"
TEMP_DIR="$(mktemp -d)"

cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

python3 -m pip install gdown

python3 - "$DRIVE_URL" "$TEMP_DIR" "$MODEL_DIR" <<'PY'
import sys
import shutil
from pathlib import Path
import gdown

url, temp, destination = sys.argv[1:]
files = gdown.download_folder(
    url=url,
    output=temp,
    quiet=False,
    use_cookies=False
)

if not files:
    raise SystemExit("Download failed or the Drive folder is empty.")

matches = list(Path(temp).rglob("wide_resnet50_2.pth"))

if not matches:
    raise SystemExit("Model weights not found in downloaded folder.")

source = matches[0].parent
target = Path(destination)
target.mkdir(parents=True, exist_ok=True)

shutil.copytree(source, target, dirs_exist_ok=True)

required = [
    target / "wide_resnet50_2.pth",
    target / "thresholds.csv",
    target / "bottle" / "memory_bank.npy",
    target / "bottle" / "pca.pkl"
]

missing = [str(p) for p in required if not p.is_file()]

if missing:
    raise SystemExit("Missing required model files:\n" + "\n".join(missing))

print("\nInspectra models downloaded successfully!")
PY

echo "Model setup complete!"
