from fastapi import APIRouter

from backend.app.config import (
    APP_VERSION,
    DB_PATH,
)


router = APIRouter(
    prefix="/api",
    tags=["Sistema"],
)


@router.get("/salud")
def salud():
    return {
        "estado": "ok",
        "base_datos": str(DB_PATH),
        "version": APP_VERSION,
    }