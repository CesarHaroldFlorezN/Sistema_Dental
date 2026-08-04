from sqlalchemy import JSON, Column, Float, Integer, String, Text

from backend.app.database.session import Base


class PagoDB(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)

    pacienteId = Column(Integer, index=True)
    citaId = Column(Integer, index=True)

    concepto = Column(String(200))
    fecha = Column(String(50))

    total = Column(Float)
    cobrado = Column(Float)
    saldo = Column(Float)

    metodo = Column(String(50))
    tipoPago = Column(String(50))
    cuotas = Column(JSON)

    creadoEn = Column(String(50))
    fechaUltPago = Column(String(50))
    nota = Column(Text)

    devuelto = Column(Float)
    creditoFavor = Column(Float)