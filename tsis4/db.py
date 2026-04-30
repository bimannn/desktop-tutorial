import psycopg2
import os
from datetime import datetime

os.environ['PGCLIENTENCODING'] = 'utf-8'

# Параметры подключения
DB_NAME = "snake_db"
DB_USER = "postgres"
DB_PASS = "Apalon228a"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    dsn = f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST} port={DB_PORT} client_encoding='UTF8'"
    return psycopg2.connect(dsn)

def save_score(username, score, level):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;", (username,))
        cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
        p_id = cur.fetchone()[0]
        cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);", (p_id, score, level))
        conn.commit()
        cur.close()
    except Exception as e:
        if conn: conn.rollback()
        print(f"DB Error: {e}")
    finally:
        if conn: conn.close()

def get_top_10():
    conn = None
    res = []
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, s.score, s.level_reached, s.played_at 
            FROM game_sessions s JOIN players p ON s.player_id = p.id 
            ORDER BY s.score DESC LIMIT 10;
        """)
        res = cur.fetchall()
        cur.close()
    except Exception as e:
        print(f"DB Error: {e}")
    finally:
        if conn: conn.close()
    return res

def get_personal_best(username):
    conn = None
    res = 0
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT MAX(score) FROM game_sessions s 
            JOIN players p ON s.player_id = p.id WHERE p.username = %s;
        """, (username,))
        row = cur.fetchone()
        if row and row[0]: res = row[0]
        cur.close()
    except Exception:
        pass
    finally:
        if conn: conn.close()
    return res