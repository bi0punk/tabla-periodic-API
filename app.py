from fastapi import FastAPI, HTTPException
from typing import Optional
import json

app = FastAPI()

with open("elements.json", "r") as file:
    tabla_periodica_data = json.load(file)

@app.get("/elementos/")
async def listar_elementos():
    """Devuelve una lista de todos los elementos de la tabla periódica"""
    return tabla_periodica_data

@app.get("/elementos/{numero_atomico}")
async def obtener_elemento(numero_atomico: int):
    """Devuelve los datos de un elemento específico según su número atómico"""
    for elemento in tabla_periodica_data:
        if elemento["atomic_number"] == str(numero_atomico):
            return elemento
    raise HTTPException(status_code=404, detail="Elemento no encontrado")


if __name__ == "__main__":
    import uvicorn
    from fastapi.openapi.docs import get_swagger_ui_html

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(openapi_url="/openapi.json", title="Documentación")

    @app.get("/openapi.json", include_in_schema=False)
    async def get_open_api_endpoint():
        return app.openapi()

    uvicorn.run(app, host="0.0.0.0", port=8000)
