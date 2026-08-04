from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.app.config import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
    CORS_ORIGINS,
    FRONTEND_ASSETS,
    FRONTEND_DIR,
)
from backend.app.database.migrations import inicializar_base_datos
from backend.app.routers import (
    citas,
    documentos,
    pacientes,
    pagos,
    planes,
    reportes,
    sistema,
)


def crear_aplicacion() -> FastAPI:
    aplicacion = FastAPI(
        title=APP_NAME,
        version=APP_VERSION,
        description=APP_DESCRIPTION,
    )

    aplicacion.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    aplicacion.include_router(sistema.router)
    aplicacion.include_router(pacientes.router)
    aplicacion.include_router(citas.router)
    aplicacion.include_router(pagos.router)
    aplicacion.include_router(planes.router)
    aplicacion.include_router(documentos.router)
    aplicacion.include_router(reportes.router)

    inicializar_base_datos()

    if FRONTEND_DIR.is_dir():
        if FRONTEND_ASSETS.is_dir():
            aplicacion.mount(
                "/assets",
                StaticFiles(directory=str(FRONTEND_ASSETS)),
                name="react-assets",
            )

        @aplicacion.get("/", include_in_schema=False)
        def mostrar_frontend():
            return FileResponse(
                FRONTEND_DIR / "index.html"
            )

        @aplicacion.get(
            "/{ruta:path}",
            include_in_schema=False,
        )
        def mostrar_ruta_react(ruta: str):
            if ruta.startswith("api/"):
                raise HTTPException(
                    status_code=404,
                    detail="Ruta API no encontrada.",
                )

            archivo = (FRONTEND_DIR / ruta).resolve()
            frontend = FRONTEND_DIR.resolve()

            try:
                archivo.relative_to(frontend)
            except ValueError as exc:
                raise HTTPException(
                    status_code=404,
                    detail="Archivo no encontrado.",
                ) from exc

            if archivo.is_file():
                return FileResponse(archivo)

            return FileResponse(
                FRONTEND_DIR / "index.html"
            )

    else:

        @aplicacion.get("/", include_in_schema=False)
        def estado_backend():
            return {
                "message": "API DentalPro activa",
                "frontend": "No compilado",
                "instruccion": (
                    "Ejecuta npm run dev "
                    "o npm run build."
                ),
            }

    return aplicacion


app = crear_aplicacion()