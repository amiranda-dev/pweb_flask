import sqlite3

DB_PATH = "banco_escola.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn