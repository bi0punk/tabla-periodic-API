from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

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

class ElementResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='ID del elemento requerido')
        args = parser.parse_args()
        element_id = args['id']
        elementos = obtener_elementos(element_id)
        if elementos:
            return {'elementos': elementos}
        else:
            return {'error': 'Elemento no encontrado'}, 404

api.add_resource(ElementResource, '/elements')

if __name__ == '__main__':
    app.run(debug=True)
