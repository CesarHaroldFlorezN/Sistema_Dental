from fastapi import APIRouter


router = APIRouter(
    prefix="/api/reportes",
    tags=["Reportes"],
)


@router.get("/estado")
def estado_reportes():
    return {
        "estado": "pendiente",
        "message": "El módulo de reportes será implementado después.",
    }