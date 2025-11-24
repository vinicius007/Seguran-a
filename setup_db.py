import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE,
    password TEXT,
    role TEXT
);
''')

cursor.execute("INSERT INTO users (cpf, password, role) VALUES ('12345678900', '1234', 'admin')")
conn.commit()
conn.close()
