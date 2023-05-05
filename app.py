from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)



@app.route('/elements', methods=['POST'])
def obtener_usuarios():
    """ Petición POST """
    element_id = request.args['id']

    print(element_id)


    """ Conexion SQLite """
    conexion = sqlite3.connect('elements.db')
    cursor = conexion.cursor()

    # Ejecutar una consulta SQL para buscar los elementos
    cursor.execute('SELECT * FROM Elements WHERE NumeroAtomico = ?;', ([element_id]))
    """ cursor.execute("SELECT * FROM Elements WHERE NumeroAtomica = ?;", [element_id]) """
    resultados = cursor.fetchall()
    print(resultados)

    # Convertir los resultados en un objeto JSON y devolverlos
    elementos = []
    for fila in resultados:
        elemento = {'Nombre': fila[0], 
                    'Número átomico': fila[1],
                    'Símbolo': fila[2],
                    'Masa' : fila[3],
                    'Masa exacta' : fila[4],
                    'Ionización' : fila[5],
                    'Afinidad electrónica' : fila[6]





        elementos.append(elemento)

    return jsonify({'Elemento': resultados})

if __name__ == '__main__':
    app.run(debug=True)
