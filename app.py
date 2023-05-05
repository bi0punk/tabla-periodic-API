from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db():
   conn = sqlite3.connect('elements.db')
   c = conn.cursor()


@app.route('/data', methods=['POST'])
def get_data():
   db = get_db()
   """ data = request.get_json() """
   data = request.args.get("id")
   id = data['id']
   print(id)
   db.execute('SELECT * FROM Elements WHERE id = ?', (id,))
   row = db.fetchone()
   if row is None:
      return jsonify({'error': 'Elemento no encontrado....Aun'})
   else:
      return jsonify({'data': row})


if __name__ == '__main__':
   app.run(debug=True)
