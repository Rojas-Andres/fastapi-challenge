"""
Test for Download manager api
"""

import os
import subprocess

import psycopg2
from psycopg2 import extensions, sql


def drop_database_and_create_database(database_name: str):
    db_params = {
        "dbname": "postgres",
        "user": os.environ.get("DATABASE_USER"),
        "password": os.environ.get("DATABASE_PASSWORD"),
        "host": os.environ.get("DATABASE_HOST"),
        "port": os.environ.get("DATABASE_PORT"),
    }
    conn = psycopg2.connect(**db_params)
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    DATABASE_NAME = f"{database_name}"
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {database_name};")
        conn.commit()
    except Exception:
        cursor.execute(f"DROP DATABASE {DATABASE_NAME};")
        conn.commit()
        print("Eliminada porque ya existe!")
        cursor.execute(f"CREATE DATABASE {database_name};")
        conn.commit()
        print("No se logro eliminar porque no estaba creada!")
    conn.close()
    print(f"Base de datos '{DATABASE_NAME}' eliminada exitosamente.")


def execute_alembic():
    """
    Execute alembic upgrade heads command to create tables in database test
    """
    print("EJECTUANDO ALEMBIC UPGRADE HEADS")
    command = ["alembic", "upgrade", "heads"]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        print("Comando ejecutado exitosamente:")
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:")
        print(e.output)


def init_testing(database_name: str):
    """
    Initialize the test environment
    """
    drop_database_and_create_database(database_name)
    execute_alembic()
    print("Test environment initialized")
