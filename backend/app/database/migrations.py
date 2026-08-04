from backend.app.database.session import Base, engine

# Importar modelos registra todas las tablas en Base.metadata.
from backend.app import models  # noqa: F401


def asegurar_compatibilidad_esquema() -> None:
    with engine.begin() as connection:
        tablas = {
            fila[0]
            for fila in connection.exec_driver_sql(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }

        if "citas" not in tablas:
            return

        columnas_citas = {
            fila[1]
            for fila in connection.exec_driver_sql(
                "PRAGMA table_info(citas)"
            ).fetchall()
        }

        if "servicios" not in columnas_citas:
            connection.exec_driver_sql(
                "ALTER TABLE citas ADD COLUMN servicios JSON"
            )

        if "horaFin" not in columnas_citas:
            connection.exec_driver_sql(
                "ALTER TABLE citas ADD COLUMN horaFin VARCHAR(50)"
            )

        if "duracionMinutos" not in columnas_citas:
            connection.exec_driver_sql(
                "ALTER TABLE citas ADD COLUMN duracionMinutos INTEGER"
            )


def inicializar_base_datos() -> None:
    Base.metadata.create_all(bind=engine)
    asegurar_compatibilidad_esquema()