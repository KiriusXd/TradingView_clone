import sqlite3
from contextlib import contextmanager
from pathlib import Path
from ..core.config import settings


def init_db():
    """Создает таблицы в базе данных, если они не существуют"""
    db_path = Path(settings.get_database_path())
    db_path.parent.mkdir(parents=True, exist_ok=True)  # Создать папку data/

    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS ohlcv (
                symbol TEXT,
                timestamp INTEGER,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume REAL,
                PRIMARY KEY (symbol, timestamp)
            )
        ''')


@contextmanager
def get_db():
    db_path = settings.get_database_path()
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
