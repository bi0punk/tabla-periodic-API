from fastapi import FastAPI, HTTPException
from typing import Optional
import json

app = FastAPI()

with open("elements.json", "r") as file:
    tabla_periodica_data = json.load(file)

@app.get("/elements/")
async def listar_elementos():
    return tabla_periodica_data

@app.get("/elements/{numero_atomico}")
async def obtener_elemento(numero_atomico: int):
    for elemento in tabla_periodica_data:
        if elemento["atomic_number"] == str(numero_atomico):
            return elemento
    raise HTTPException(status_code=404, detail="Elemento no encontrado / Not Found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
