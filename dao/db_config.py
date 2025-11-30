import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_VCB9LZNrAQF5@ep-noisy-tree-ads28vic-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn