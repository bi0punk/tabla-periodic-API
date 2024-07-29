from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import uvicorn

app = FastAPI()

# Definir el modelo de datos
class Elemento(BaseModel):
    name: str
    symbol: str
    atomic_number: str
    mass: str
    exact_mass: Optional[str] = None
    ionization: Optional[str] = None
    electron_affinity: Optional[str] = None
    electronegativity: Optional[str] = None
    covalent_radius: Optional[str] = None
    van_der_waals_radius: Optional[str] = None
    melting_point: Optional[str] = None
    boiling_point: Optional[str] = None
    family: str

    class Config:
        # Esto permite que los campos opcionales sean None si no están presentes
        anystr_strip_whitespace = True

# Cargar los datos de manera eficiente
def cargar_datos():
    with open("elements.json", "r") as file:
        return json.load(file)

# Almacenar los datos cargados
tabla_periodica_data = cargar_datos()

@app.get("/elementos/", response_model=List[Elemento])
async def listar_elementos():
    """Devuelve una lista de todos los elementos de la tabla periódica"""
    return tabla_periodica_data

@app.get("/elementos/{numero_atomico}", response_model=Elemento)
async def obtener_elemento(numero_atomico: int):
    """Devuelve los datos de un elemento específico según su número atómico"""
    for elemento in tabla_periodica_data:
        if elemento["atomic_number"] == str(numero_atomico):
            return elemento
    raise HTTPException(status_code=404, detail="Elemento no encontrado")

@app.get("/search/")
async def buscar_elemento(nombre: Optional[str] = Query(None, description="Nombre del elemento")):
    """Busca un elemento por nombre"""
    if nombre:
        resultados = [elemento for elemento in tabla_periodica_data if nombre.lower() in elemento["name"].lower()]
        if resultados:
            return resultados
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    raise HTTPException(status_code=400, detail="Nombre del elemento es requerido")

# Personalizar la documentación
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    from fastapi.openapi.docs import get_swagger_ui_html
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Documentación de la API")

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
