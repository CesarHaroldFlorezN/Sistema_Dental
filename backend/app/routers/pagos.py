from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.models import PagoDB
from backend.app.schemas.pago import OperacionPagoPayload
from backend.app.services import pagos_service
from backend.app.utils import serializar_modelo


router = APIRouter(
    prefix="/api",
    tags=["Finanzas"],
)


@router.get("/pagos")
def listar_pagos(
    db: Session = Depends(get_db),
):
    pagos = db.query(PagoDB).order_by(
        PagoDB.id.desc()
    ).all()

    return [
        serializar_modelo(pago)
        for pago in pagos
    ]


@router.post("/operaciones/pagos/{pago_id}/registrar")
def registrar_pago(
    pago_id: int,
    payload: OperacionPagoPayload,
    db: Session = Depends(get_db),
):
    return pagos_service.registrar_pago(
        db,
        pago_id,
        payload,
    )


@router.post("/operaciones/pagos/{pago_id}/anular")
def anular_pago(
    pago_id: int,
    payload: OperacionPagoPayload,
    db: Session = Depends(get_db),
):
    return pagos_service.anular_pago(
        db,
        pago_id,
        payload,
    )


@router.post("/operaciones/pagos/{pago_id}/devolver")
def devolver_pago(
    pago_id: int,
    payload: OperacionPagoPayload,
    db: Session = Depends(get_db),
):
    return pagos_service.devolver_pago(
        db,
        pago_id,
        payload,
    )


@router.get("/pacientes/{paciente_id}/cuenta")
def cuenta_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
):
    return pagos_service.obtener_cuenta_paciente(
        db,
        paciente_id,
    )