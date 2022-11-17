import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(user="cvcode",
                            password="cvcode",
                            host="postgre_db",
                            port="5432",
                            database="cvcode_database")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks=tasks)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        wallet = request.form['wallet']
        task = request.form['task']


        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (wallet, task)'
                    'VALUES (%s, %s)',
                    (wallet, task))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/vacancy')
def vacancy():
    return render_template('vacancy.html')


if __name__ == '__main__':
    app.run(host="web_app", port="7654")
