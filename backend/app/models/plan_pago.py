from sqlalchemy import JSON, Column, Float, Integer, String

from backend.app.database.session import Base


class PlanPagoDB(Base):
    __tablename__ = "planPagos"

    id = Column(Integer, primary_key=True, index=True)

    pacienteId = Column(Integer, index=True)
    pagoId = Column(Integer, index=True)
    citaId = Column(Integer, index=True)

    concepto = Column(String(200))
    totalAcordado = Column(Float)
    anticipo = Column(Float)
    metodoPreferido = Column(String(50))
    estado = Column(String(50))

    cuotas = Column(JSON)
    totalCuotas = Column(Float)
    cobrado = Column(Float)
    saldo = Column(Float)

    fechaCreacion = Column(String(50))
    creadoEn = Column(String(50))