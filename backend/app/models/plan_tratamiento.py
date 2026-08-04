from sqlalchemy import Column, Float, Integer, String, Text

from backend.app.database.session import Base


class PlanDB(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True, index=True)

    pacienteId = Column(Integer, index=True)
    nombre = Column(String(150))
    tipo = Column(String(100))
    duracion = Column(String(50))
    costo = Column(Float)
    nSesiones = Column(Integer)
    descripcion = Column(Text)
    estado = Column(String(50))
    creadoEn = Column(String(50))