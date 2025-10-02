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

cur.execute('''
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    course TEXT NOT NULL,
    message TEXT
)
''')

# Админ
username = os.getenv("ADMIN_USERNAME", "admin")
password = generate_password_hash(os.getenv("ADMIN_PASSWORD", "adminchik123"))
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

conn.commit()
conn.close()

print("База инициализирована. Админ:", username)