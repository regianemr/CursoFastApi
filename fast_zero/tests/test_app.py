from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização do teste)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # afirmação
    assert response.json() == {'mensagem': 'Olá, mundo!'}


def test_html_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização do teste)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # afirmação
    assert response.json() == {'mensagem': 'Olá, mundo!'}
