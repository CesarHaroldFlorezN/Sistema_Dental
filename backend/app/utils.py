from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Any


def ahora_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def fecha_local_iso() -> str:
    return datetime.now().astimezone().date().isoformat()


def serializar_modelo(registro) -> dict[str, Any]:
    return {
        columna.name: getattr(registro, columna.name)
        for columna in registro.__table__.columns
    }


def redondear_dinero(valor: Any) -> float:
    decimal = Decimal(str(valor or 0))

    return float(
        decimal.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )
    )


def limpiar_valor_csv(valor: Any) -> str:
    return str(valor or "").strip()