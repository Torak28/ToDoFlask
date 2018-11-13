from flask import Flask, g, render_template, flash, redirect, url_for, request
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)


app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='ToDoFlask'
))


def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    if not g.get('db'):  # jeżeli brak połączenia, to je tworzymy
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con  # zapisujemy połączenie w kontekście aplikacji
    return g.db  # zwracamy połączenie z bazą


@app.teardown_appcontext
def close_db(error):
    """Zamykanie połączenia z bazą"""
    if g.get('db'):
        g.db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/zadania', methods=['GET', 'POST'])
def zadania():
    error = None
    if request.method == 'POST':
        zadanie = request.form['zadanie'].strip()
        if len(zadanie) > 0:
            zrobione = '0'
            data_pub = datetime.now()
            db = get_db()
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?);',
                       [None, zadanie, zrobione, data_pub])
            db.commit()
            flash('Add new task.', 'success')
            return redirect(url_for('zadania'))

        error = 'You can\'t add empty task!'  # komunikat o błędzie

    db = get_db()
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_pub DESC;')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania, error=error)

@app.route('/zrobione', methods=['POST'])
def zrobione():
    """Zmiana statusu zadania na wykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('UPDATE zadania SET zrobione=1 WHERE id=?', [zadanie_id])
    db.commit()
    flash('Task Done!', 'success')
    return redirect(url_for('zadania'))


@app.route('/niezrobione', methods=['POST'])
def niezrobione():
    """Zmiana statusu zadania na niewykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('UPDATE zadania SET zrobione=0 WHERE id=?', [zadanie_id])
    db.commit()
    flash('Task Undone :c', 'warning')
    return redirect(url_for('zadania'))


@app.route('/usuniete', methods=['POST'])
def usuniete():
    """Usuniecie zadania gdy wykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('DELETE FROM zadania WHERE id=?', [zadanie_id])
    db.commit()
    flash('Task deleted.', 'warning')
    return redirect(url_for('zadania'))


@app.route('/usun', methods=['POST'])
def usun():
    """Usuniecie zadan wykonanych."""
    db = get_db()
    db.execute('DELETE FROM zadania WHERE zrobione=1;')
    db.commit()
    flash('All done tasks were removed', 'warning')
    return redirect(url_for('zadania'))


if __name__ == '__main__':
    app.run(debug=True)
