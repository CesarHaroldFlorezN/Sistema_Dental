from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile,
)
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.services import documentos_service


router = APIRouter(
    prefix="/api/pacientes/{paciente_id}/documentos",
    tags=["Documentos"],
)


@router.get("")
def listar_documentos(
    paciente_id: int,
    db: Session = Depends(get_db),
):
    return documentos_service.listar_documentos(
        db,
        paciente_id,
    )


@router.post("")
async def subir_documento(
    paciente_id: int,
    file: UploadFile = File(...),
    descripcion: str = Form(""),
    db: Session = Depends(get_db),
):
    return await documentos_service.subir_documento(
        db,
        paciente_id,
        file,
        descripcion,
    )


@router.get("/{documento_id}/descargar")
def descargar_documento(
    paciente_id: int,
    documento_id: int,
    db: Session = Depends(get_db),
):
    return documentos_service.descargar_documento(
        db,
        paciente_id,
        documento_id,
    )


@router.delete("/{documento_id}")
def eliminar_documento(
    paciente_id: int,
    documento_id: int,
    db: Session = Depends(get_db),
):
    return documentos_service.eliminar_documento(
        db,
        paciente_id,
        documento_id,
    )