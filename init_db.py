import sqlite3, os
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

db_path = os.path.join("instance", "site.db")
os.makedirs("instance", exist_ok=True)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Таблицы
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS contacts")

cur.execute("""
CREATE TABLE users (