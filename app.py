from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'


def get_db():
   db = getattr('_database', None)
   if db is None:
      db = _database = sqlite3.connect(DATABASE)
   return db


@app.teardown_appcontext
def close_connection(exception):
   db = getattr('_database', None)
   if db is not None:
      db.close()


@app.route('/data', methods=['POST'])
def get_data():
   db = get_db()
   cursor = db.cursor()
   data = request.get_json()
   id = data['id']
   cursor.execute('SELECT * FROM Elements WHERE id = ?', (id,))
   row = cursor.fetchone()
   if row is None:
      return jsonify({'error': 'Elemento no encontrado....Aun'})
   else:
      return jsonify({'data': row})


if __name__ == '__main__':
   app.run(debug=True)
