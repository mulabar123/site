import sqlite3
#database.db

def create_table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        content VARCHAR
    )''')
    conn.commit()
    cur.close()
    conn.close()

def add_post(title, content):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO posts (title, content) VALUES (?, ?)''', [title, content])
    conn.commit()
    cur.close()
    conn.close()

def get_posts():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM posts''')
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result
