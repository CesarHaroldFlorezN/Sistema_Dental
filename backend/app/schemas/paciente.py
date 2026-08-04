from pydantic import BaseModel, ConfigDict, EmailStr, Field


class PacienteBase(BaseModel):
    codigo_ficha: str | None = Field(default=None, max_length=50)
    cedula: str = Field(min_length=1, max_length=50)
    nombre: str = Field(min_length=2, max_length=100)
    telefono: str | None = Field(default=None, max_length=50)
    correo: EmailStr | None = None
    fechaNacimiento: str | None = Field(default=None, max_length=50)
    genero: str | None = Field(default=None, max_length=50)
    direccion: str | None = Field(default=None, max_length=200)
    alergias: str | None = None
    medicamentos: str | None = None


class PacienteCrear(PacienteBase):
    pass


class PacienteActualizar(PacienteBase):
    pass


class PacienteRespuesta(PacienteBase):
    id: int
    fechaReg: str | None = None

    model_config = ConfigDict(from_attributes=True)