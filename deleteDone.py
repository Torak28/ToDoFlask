import sqlite3

def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    con = sqlite3.connect('db.sqlite')
    con.row_factory = sqlite3.Row
    return con

db = get_db()
db.execute('DELETE FROM zadania WHERE zrobione=1;')
db.commit()
db.close()
