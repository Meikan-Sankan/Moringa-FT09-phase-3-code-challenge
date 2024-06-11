import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('magazine.db')
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return conn