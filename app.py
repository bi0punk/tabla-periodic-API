from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)



@app.route('/elements', methods=['POST'])
def obtener_usuarios():
    # Obtener los parámetros de la petición POST
    element_id = request.args['id']

    print(element_id)


    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect('elements.db')
    cursor = conexion.cursor()

    # Ejecutar una consulta SQL para buscar los usuarios
    cursor.execute('SELECT * FROM Elements WHERE NumeroAtomico = ?', (element_id))
    resultados = cursor.fetchall()
    print(resultados)

    # Convertir los resultados en un objeto JSON y devolverlos
    usuarios = []
    """ for fila in resultados:
        usuario = {'id': fila[0], 'nombre': fila[1], 'apellido': fila[2]}
        usuarios.append(usuario) """

    return jsonify({'Elemento': resultados})

if __name__ == '__main__':
    app.run(debug=True)
