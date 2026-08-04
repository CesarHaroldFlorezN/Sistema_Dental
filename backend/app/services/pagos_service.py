from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.models import (
    MovimientoCuentaDB,
    PagoDB,
    PlanPagoDB,
)
from backend.app.schemas.pago import OperacionPagoPayload
from backend.app.utils import (
    ahora_iso,
    fecha_local_iso,
    redondear_dinero,
    serializar_modelo,
)


def obtener_pago(db: Session, pago_id: int) -> PagoDB:
    pago = (
        db.query(PagoDB)
        .filter(PagoDB.id == pago_id)
        .first()
    )

    if not pago:
        raise HTTPException(
            status_code=404,
            detail="El registro de pago no existe.",
        )

    return pago