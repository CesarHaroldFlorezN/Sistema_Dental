from pathlib import Path
import sys


APP_NAME = "DentalPro"
APP_VERSION = "1.4.0"
APP_DESCRIPTION = "Backend local para gestión clínica, agenda y finanzas."


if getattr(sys, "frozen", False):
    PROJECT_ROOT = Path(sys.executable).resolve().parent
else:
    # proyecto/backend/app/config.py
    # parents[0] = app
    # parents[1] = backend
    # parents[2] = raíz del proyecto
    PROJECT_ROOT = Path(__file__).resolve().parents[2]


DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "dentalpro.db"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

DOCUMENTOS_DIR = DATA_DIR / "documentos"
DOCUMENTOS_DIR.mkdir(parents=True, exist_ok=True)

BACKUPS_DIR = PROJECT_ROOT / "backups"
BACKUPS_DIR.mkdir(parents=True, exist_ok=True)


if getattr(sys, "frozen", False):
    FRONTEND_DIR = Path(sys._MEIPASS) / "frontend"
else:
    FRONTEND_DIR = PROJECT_ROOT / "frontend-moderno" / "dist"


FRONTEND_ASSETS = FRONTEND_DIR / "assets"

CORS_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]