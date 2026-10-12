# tabla-periodic-API

API REST desarrollada con FastAPI que proporciona información sobre los 118 elementos de la tabla periódica. Los datos se sirven desde un JSON embebido en el repositorio.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)](https://fastapi.tiangolo.com)
[![CI](https://github.com/bi0punk/tabla-periodic-API/actions/workflows/ci.yml/badge.svg)](https://github.com/bi0punk/tabla-periodic-API/actions/workflows/ci.yml)

## Contenido

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Stack](#stack)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Documentación interactiva](#documentación-interactiva)
- [Tests / CI](#tests--ci)
- [Roadmap](#roadmap)
- [Licencia](#licencia)

## Características

- Listado de los 118 elementos de la tabla periódica
- Obtención de un elemento por número atómico (1-118)
- Búsqueda por nombre con coincidencia parcial, insensible a mayúsculas
- Datos servidos desde `database/elements.json` (en español), con `elements.db` como respaldo
- Documentación interactiva automática (Swagger UI y ReDoc)

## Arquitectura

```mermaid
flowchart TD
  C[Cliente HTTP] -->|GET /elementos/| L[listar_elementos]
  C -->|GET /elementos/{n}| O[obtener_elemento]
  C -->|GET /search/?nombre=...| S[buscar_elemento]
  L --> D[tabla_periodica_data cargada de elements.json]
  O --> D
  S --> D
  O -->|fuera de rango 1-118| E400[400]
  O -->|no encontrado| E404[404]
  S -->|sin nombre| E400
  S -->|sin coincidencias| E404
  D --> J[database/elements.json]
  D --> B[database/elements.db]
```

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic (modelos de datos)
- pytest + httpx (pruebas)

## Estructura del repositorio

```
tabla-periodic-API/
├── app/
│   └── app.py                 # Modelos, rutas y arranque
├── database/
│   ├── elements.json          # Datos de los 118 elementos
│   └── elements.db            # Base de datos SQLite de respaldo
├── test/
│   ├── test_app.py
│   └── test_routes.py
├── .github/workflows/
│   └── ci.yml
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

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

## Uso

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

Retorna `400` si el número atómico está fuera del rango 1-118.

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

## Tests / CI

```sh
pip install -r requirements-dev.txt
pytest
```

GitHub Actions (`.github/workflows/ci.yml`) ejecuta ruff lint + pytest sobre Python 3.12 en push/PR a `main`/`master`.

## Roadmap

- [x] Listado de los 118 elementos
- [x] Elemento por número atómico
- [x] Búsqueda por nombre
- [ ] Filtros por familia/química
- [ ] Paginación en `/elementos/`
- [ ] Soporte multi-idioma de los datos

## Licencia

MIT