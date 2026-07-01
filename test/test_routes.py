from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_search_por_nombre_parcial():
    # Los nombres están en español (Hidrógeno, Oxígeno...); "geno" aparece en ambos.
    response = client.get("/search/", params={"nombre": "geno"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(el["symbol"] == "H" for el in data)
    assert any(el["symbol"] == "O" for el in data)


def test_search_por_nombre_inexistente():
    response = client.get("/search/", params={"nombre": "elementoinexistente"})
    assert response.status_code == 404


def test_search_sin_parametro_retorna_400():
    response = client.get("/search/")
    assert response.status_code == 400
    assert "requerido" in response.json()["detail"].lower()


def test_search_es_case_insensitive():
    r_lower = client.get("/search/", params={"nombre": "geno"})
    r_upper = client.get("/search/", params={"nombre": "GENO"})
    assert r_lower.status_code == 200
    assert r_upper.status_code == 200
    assert r_lower.json() == r_upper.json()


def test_endpoint_docs_disponible():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_json_disponible():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"]