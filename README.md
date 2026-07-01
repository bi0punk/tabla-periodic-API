![tabla-periodic-API](https://socialify.git.ci/bi0punk/tabla-periodic-API/image?language=1&owner=1&name=1&stargazers=1&theme=Light)

# Tabla Periódica API

API desarrollada con FastAPI que proporciona información sobre los 118 elementos de la tabla periódica. Los datos se sirven desde un JSON embebido en el repositorio.

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn

## Instalación

1. Clona este repositorio:

   ```sh
   git clone https://github.com/bi0punk/tabla-periodic-API.git
   cd tabla-periodic-API
   ```

2. Crea y activa un entorno virtual:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

## Archivos

- `app/app.py`: código principal de la API (modelos, rutas y arranque).
- `database/elements.json`: datos de los elementos (118 elementos, en español).
- `database/elements.db`: base de datos SQLite de respaldo.
- `test/test_app.py`, `test/test_routes.py`: pruebas con `TestClient`.

## Ejecución

Para iniciar la aplicación:

```sh
uvicorn app.app:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

Para ejecutar la suite de pruebas:

```sh
pip install -r requirements-dev.txt
pytest
```

## Endpoints

### Listar elementos

- **URL:** `/elementos/`
- **Método:** `GET`
- **Descripción:** Devuelve una lista con los 118 elementos.

Respuesta de ejemplo:

```json
[
  {
    "name": "Hidrógeno",
    "symbol": "H",
    "atomic_number": "1",
    "mass": "1,00794 u",
    "exact_mass": null,
    "ionization": null,
    "electron_affinity": null,
    "electronegativity": null,
    "covalent_radius": null,
    "van_der_waals_radius": null,
    "melting_point": null,
    "boiling_point": null,
    "family": "Non-Metal"
  }
]
```

### Obtener elemento por número atómico

- **URL:** `/elementos/{numero_atomico}`
- **Método:** `GET`
- **Descripción:** Devuelve los datos de un elemento específico según su número atómico.
- **Parámetros:** `numero_atomico` (int) entre 1 y 118.

Ejemplo: `GET /elementos/1`

```json
{
  "name": "Hidrógeno",
  "symbol": "H",
  "atomic_number": "1",
  "mass": "1,00794 u",
  "exact_mass": null,
  "ionization": null,
  "electron_affinity": null,
  "electronegativity": null,
  "covalent_radius": null,
  "van_der_waals_radius": null,
  "melting_point": null,
  "boiling_point": null,
  "family": "Non-Metal"
}
```

Retorna `400` si el número atómico está fuera del rango 1–118.

### Buscar elemento por nombre

- **URL:** `/search/`
- **Método:** `GET`
- **Descripción:** Busca elementos por nombre (coincidencia parcial, insensible a mayúsculas).
- **Parámetro de query:** `nombre` (str)

Ejemplo: `GET /search/?nombre=geno`

```json
[
  {
    "name": "Hidrógeno",
    "symbol": "H",
    "atomic_number": "1",
    "mass": "1,00794 u",
    "family": "Non-Metal"
  }
]
```

Retorna `400` si no se indica `nombre` y `404` si no hay coincidencias.

## Documentación interactiva

FastAPI expone automáticamente:

- `GET /docs` — Swagger UI
- `GET /redoc` — ReDoc

## Licencia

MIT