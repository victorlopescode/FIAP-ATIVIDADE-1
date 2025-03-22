import sqlite3

def create_connection():
    conn = sqlite3.connect('dados.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY,
            cultura TEXT NOT NULL,
            area REAL NOT NULL,
            insumo REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()