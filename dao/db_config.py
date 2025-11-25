import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_cdp8TWDCsb3r@ep-orange-art-a4cwlfj4-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn