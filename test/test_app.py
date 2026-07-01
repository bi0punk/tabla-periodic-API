from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_listar_elementos_devuelve_118():
    response = client.get("/elementos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 118


def test_listar_elementos_primer_elemento_hydrogeno():
    response = client.get("/elementos/")
    primero = response.json()[0]
    assert primero["symbol"] == "H"
    assert primero["atomic_number"] == "1"
    assert "name" in primero
    assert "family" in primero


def test_obtener_elemento_por_numero_atomico_valido():
    response = client.get("/elementos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "H"


def test_obtener_elemento_por_numero_atomico_fuera_de_rango():
    response = client.get("/elementos/200")
    assert response.status_code == 400
    assert "inválido" in response.json()["detail"].lower() or "invalid" in response.json()["detail"].lower()


def test_obtener_elemento_no_existente():
    # 119 está fuera del rango 1..118 y por tanto es 400, no 404.
    # Probamos un número dentro de rango pero inexistente no es posible
    # porque la secuencia 1..118 está completa; validamos el límite superior.
    response = client.get("/elementos/118")
    assert response.status_code == 200
    assert response.json()["atomic_number"] == "118"