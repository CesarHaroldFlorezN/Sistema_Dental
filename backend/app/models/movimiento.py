from sqlalchemy import Column, Float, Integer, String, Text

from backend.app.database.session import Base


class MovimientoCuentaDB(Base):
    __tablename__ = "movimientosCuenta"

    id = Column(Integer, primary_key=True, index=True)

    pacienteId = Column(Integer, index=True)
    citaId = Column(Integer, nullable=True, index=True)
    pagoId = Column(Integer, nullable=True, index=True)

    tipo = Column(String(50), index=True)
    descripcion = Column(String(250))

    cargo = Column(Float, default=0)
    abono = Column(Float, default=0)

    fecha = Column(String(50), index=True)
    metodo = Column(String(100))
    referencia = Column(String(150))
    motivo = Column(Text)
    usuario = Column(String(100))
    creadoEn = Column(String(50))