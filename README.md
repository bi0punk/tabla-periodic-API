# Tabla Periódica API

Esta es una API desarrollada con FastAPI que proporciona información sobre los elementos de la tabla periódica.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu-usuario/tabla-periodica-api.git
    cd tabla-periodica-api
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Archivos

- `main.py`: Contiene el código principal de la API.
- `elements.json`: Archivo JSON con los datos de los elementos de la tabla periódica.

## Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando:

```sh
uvicorn main:app --reload

La aplicación estará disponible en http://127.0.0.1:8000.
Endpoints
Listar Elementos

    URL: /elementos/
    Método: GET
    Descripción: Devuelve una lista de todos los elementos de la tabla periódica.
    Respuesta de ejemplo:

    json

    [
        {
            "name": "Hydrogen",
            "symbol": "H",
            "atomic_number": "1",
            "mass": "1.008",
            "exact_mass": null,
            "ionization": null,
            "electron_affinity": null,
            "electronegativity": null,
            "covalent_radius": null,
            "van_der_waals_radius": null,
            "melting_point": null,
            "boiling_point": null,
            "family": "Nonmetal"
        },
        ...
    ]

Obtener Elemento por Número Atómico

    URL: /elementos/{numero_atomico}
    Método: GET
    Descripción: Devuelve los datos de un elemento específico según su número atómico.
    Parámetros:
        numero_atomico (int): Número atómico del elemento.
    Respuesta de ejemplo:

    json

    {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": "1",
        "mass": "1.008",
        "exact_mass": null,
        "ionization": null,
        "electron_affinity": null,
        "electronegativity": null,
        "covalent_radius": null,
        "van_der_waals_radius": null,
        "melting_point": null,
        "boiling_point": null,
        "family": "Nonmetal"
    }

Buscar Elemento por Nombre

    URL: /search/
    Método: GET
    Descripción: Busca un elemento por nombre.
    Parámetros:
        nombre (str): Nombre del elemento (opcional).
    Respuesta de ejemplo:

    json

[
    {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": "1",
        "mass": "1.008",
        "exact_mass": null,
        "ionization": null,
        "electron_affinity": null,
        "electronegativity": null,
        "covalent_radius": null,
        "van_der_waals_radius": null,
        "melting_point": null,
        "boiling_point": null,
        "family": "Nonmetal"
    }
]
