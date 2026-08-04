from pydantic import BaseModel, Field


class PlanTratamientoPayload(BaseModel):
    pacienteId: int = Field(gt=0)
    nombre: str = Field(min_length=2, max_length=150)
    tipo: str = Field(default="", max_length=100)
    duracion: str = Field(default="", max_length=50)
    costo: float = Field(default=0, ge=0)
    nSesiones: int = Field(default=1, ge=1, le=100)
    descripcion: str = Field(default="", max_length=5000)
    estado: str = Field(default="activo", max_length=50)


class PlanPagoPayload(BaseModel):
    pacienteId: int = Field(gt=0)
    pagoId: int | None = None
    citaId: int | None = None

    concepto: str = Field(min_length=2, max_length=200)
    totalAcordado: float = Field(gt=0)
    anticipo: float = Field(default=0, ge=0)
    metodoPreferido: str = Field(default="Efectivo", max_length=50)

    estado: str = Field(default="activo", max_length=50)
    cuotas: list[dict] = Field(default_factory=list)