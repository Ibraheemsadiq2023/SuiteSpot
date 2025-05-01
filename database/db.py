import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'suitespot.db')

def connect_db():
    """
    Establishes a connection to the SQLite database (creates file if not exists).
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # for dict-like cursor
    return conn


def initialize_schema():
    """
    Reads and executes the SQL statements in schema.sql to set up tables.
    """
    schema_file = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with connect_db() as conn:
        cursor = conn.cursor()
        with open(schema_file, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()


if __name__ == '__main__':
    initialize_schema()
    print(f"Initialized database at {DB_PATH}")
