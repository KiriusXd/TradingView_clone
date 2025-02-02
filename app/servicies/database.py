# app/services/database.py
import sqlite3
from contextlib import contextmanager
from ..core.config import settings


@contextmanager
def get_db():
    db_path = settings.get_database_path()
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
