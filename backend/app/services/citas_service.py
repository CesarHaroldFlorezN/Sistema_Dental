from datetime import datetime
from typing import Any

from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from backend.app.models import CitaDB, PacienteDB, PagoDB, PlanDB
from backend.app.schemas.cita import CitaPagoPayload
from backend.app.utils import ahora_iso, redondear_dinero, serializar_modelo


ESTADOS_QUE_BLOQUEAN_HORARIO = {
    "pendiente",
    "confirmada",
    "en_espera",
    "en_atencion",
}

TRANSICIONES_ESTADO = {
    "pendiente": {
        "confirmada",
        "en_espera",
        "en_atencion",
        "no_asistio",
        "cancelada",
    },
    "confirmada": {
        "pendiente",
        "en_espera",
        "en_atencion",
        "no_asistio",
        "cancelada",
    },
    "en_espera": {
        "confirmada",
        "en_atencion",
        "no_asistio",
        "cancelada",
    },
    "en_atencion": {"completada", "cancelada"},
    "no_asistio": {"pendiente"},
    "cancelada": {"pendiente"},
    "completada": set(),
}


def convertir_hora_a_minutos(hora: str) -> int:
    try:
        horas, minutos = [
            int(parte)
            for parte in hora.split(":", 1)
        ]
    except (TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=422,
            detail="La hora no tiene un formato válido.",
        ) from exc

    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
        raise HTTPException(
            status_code=422,
            detail="La hora no tiene un formato válido.",
        )

    return horas * 60 + minutos


def minutos_a_hora(total_minutos: int) -> str:
    if not 0 <= total_minutos < 24 * 60:
        raise HTTPException(
            status_code=422,
            detail="La cita debe terminar antes de medianoche.",
        )

    return (
        f"{total_minutos // 60:02d}:"
        f"{total_minutos % 60:02d}"
    )


def resolver_rango_horario(
    fecha: str,
    hora_inicio: str,
    hora_fin: str | None,
    duracion_minutos: int,
) -> tuple[int, int, str, int]:
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail="La fecha no tiene un formato válido.",
        ) from exc

    inicio_min = convertir_hora_a_minutos(hora_inicio)
    duracion = int(duracion_minutos or 60)

    if hora_fin:
        fin_min = convertir_hora_a_minutos(hora_fin)
        duracion = fin_min - inicio_min
    else:
        fin_min = inicio_min + duracion
        hora_fin = minutos_a_hora(fin_min)

    if duracion < 5:
        raise HTTPException(
            status_code=422,
            detail="La hora final debe ser posterior al inicio.",
        )

    if duracion > 720 or fin_min >= 24 * 60:
        raise HTTPException(
            status_code=422,
            detail=(
                "La cita no puede superar 12 horas "
                "ni terminar a medianoche."
            ),
        )

    return inicio_min, fin_min, hora_fin, duracion