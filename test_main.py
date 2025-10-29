from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_endpoint_datos_invalidos():
    response = client.get("/evaluaciones/tarjetas?edad=-17&ingresos=-2000")
    assert response.status_code == 400
    assert response.json()["detail"] == "Datos Invalidos"


def test_endpoint_rechazado():
    response = client.get("/evaluaciones/tarjetas?edad=17&ingresos=2000")
    assert response.status_code == 200
    assert response.json()["status"] == "Rechazado"


def test_endpoint_regular():
    response = client.get("/evaluaciones/tarjetas?edad=22&ingresos=2000")
    assert response.status_code == 200
    assert response.json()["status"] == "Aprobado"
