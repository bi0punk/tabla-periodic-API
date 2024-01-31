from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def obtener_elementos(element_id):
    try:
        conexion = sqlite3.connect('elements.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Elements WHERE NumeroAtomico = ?;', (element_id,))
        resultados = cursor.fetchall()
        elementos = []
        for fila in resultados:
            elemento = {
                'Nombre': fila[0], 
                'Número átomico': fila[1],
                'Símbolo': fila[2],
                'Masa': fila[3],
                'Masa exacta': fila[4],
                'Ionización': fila[5],
                'Afinidad electrónica': fila[6],
                'Electronegatividad': fila[7],
                'Radio covalente': fila[8],
                'Radio de Van der Waals': fila[9],
                'Punto de fusión': fila[10],
                'Punto de ebullición': fila[11],
                'Familia': fila[12]
            }
            elementos.append(elemento)
        return elementos
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        return []

@app.route('/elements', methods=['POST'])
def obtener_usuarios():
    element_id = request.args.get('id')
    if element_id is not None:
        elementos = obtener_elementos(element_id)
        return jsonify(elementos)
    else:
        return jsonify({'error': 'Parámetro "id" no proporcionado'})

if __name__ == '__main__':
    app.run(debug=True)
