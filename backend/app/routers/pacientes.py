import csv
import io

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.paciente import (
    PacienteActualizar,
    PacienteCrear,
)
from backend.app.services import pacientes_service


router = APIRouter(
    prefix="/api",
    tags=["Pacientes"],
)


@router.get("/pacientes")
def listar_pacientes(
    db: Session = Depends(get_db),
):
    return pacientes_service.listar_pacientes(db)


@router.post("/pacientes")
def crear_paciente(
    payload: PacienteCrear,
    db: Session = Depends(get_db),
):
    return pacientes_service.crear_paciente(
        db,
        payload,
    )


@router.put("/pacientes/{paciente_id}")
def actualizar_paciente(
    paciente_id: int,
    payload: PacienteActualizar,
    db: Session = Depends(get_db),
):
    return pacientes_service.actualizar_paciente(
        db,
        paciente_id,
        payload,
    )


@router.delete("/pacientes/{paciente_id}")
def eliminar_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
):
    return pacientes_service.eliminar_paciente(
        db,
        paciente_id,
    )


@router.get("/exportar/pacientes")
def exportar_pacientes(
    db: Session = Depends(get_db),
):
    return pacientes_service.exportar_pacientes(db)


@router.post("/importar/pacientes")
async def importar_pacientes(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return await pacientes_service.importar_pacientes(
        db,
        file,
    )