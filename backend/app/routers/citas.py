from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.cita import (
    CambioEstadoPayload,
    CitaPagoPayload,
    ReprogramarCitaPayload,
)
from backend.app.services import citas_service


router = APIRouter(
    prefix="/api/operaciones/citas",
    tags=["Citas"],
)


@router.get("")
def listar_citas(
    db: Session = Depends(get_db),
):
    return citas_service.listar_citas(db)


@router.post("")
def crear_cita(
    payload: CitaPagoPayload,
    db: Session = Depends(get_db),
):
    return citas_service.crear_cita_con_pago(
        db,
        payload,
    )


@router.put("/{cita_id}")
def actualizar_cita(
    cita_id: int,
    payload: CitaPagoPayload,
    db: Session = Depends(get_db),
):
    return citas_service.actualizar_cita_con_pago(
        db,
        cita_id,
        payload,
    )


@router.patch("/{cita_id}/reprogramar")
def reprogramar_cita(
    cita_id: int,
    payload: ReprogramarCitaPayload,
    db: Session = Depends(get_db),
):
    return citas_service.reprogramar_cita(
        db,
        cita_id,
        payload,
    )


@router.patch("/{cita_id}/estado")
def cambiar_estado(
    cita_id: int,
    payload: CambioEstadoPayload,
    db: Session = Depends(get_db),
):
    return citas_service.cambiar_estado_cita(
        db,
        cita_id,
        payload,
    )


@router.delete("/{cita_id}")
def eliminar_cita(
    cita_id: int,
    db: Session = Depends(get_db),
):
    return citas_service.eliminar_cita_con_pago(
        db,
        cita_id,
    )


