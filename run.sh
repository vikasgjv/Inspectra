
#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

VENV="$ROOT_DIR/backend/.venv"

if [ ! -d "$VENV" ]; then
    echo "Virtual environment not found. Run ./setup.sh first."
    exit 1
fi

source "$VENV/bin/activate"

echo "Starting Inspectra..."

python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
