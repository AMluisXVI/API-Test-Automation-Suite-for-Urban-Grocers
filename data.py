import pytest
import sender_stand_request as req
import data

def get_new_user_token():
    response = req.post_create_new_user(data.user_body)
    assert response is not None, "Error: No se pudo obtener el token de autenticación"
    return response.json()["authToken"]

def get_kit_name(kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = kit_name
    return current_kit_name

def positive_assert_201(kit_body):
    response = req.post_create_new_kit(kit_body, get_new_user_token())
    assert response.status_code == 201, f"Error en la creación del kit: {response.status_code}"
    assert response.json().get("name") == kit_body["name"], "El campo 'name' no coincide"

def negative_assert_code_400(kit_body):
    response = req.post_create_new_kit(kit_body, get_new_user_token())
    assert response.status_code == 400, f"Error esperado 400, pero se obtuvo: {response.status_code}"

def test_create_kit_valid_cases():
    valid_kit_bodies = [
        get_kit_name("a"),
        get_kit_name("El valor de prueba para esta comprobación será inferior a 51 caracteres"),
        get_kit_name("N%@*"),
        get_kit_name(" A Aaa "),
        get_kit_name("123")
    ]
    for kit_body in valid_kit_bodies:
        positive_assert_201(kit_body)

def test_create_kit_invalid_cases():
    invalid_kit_bodies = [
        get_kit_name(""),
        get_kit_name("a" * 512),
        {},
        get_kit_name(123)
    ]
    for kit_body in invalid_kit_bodies:
        negative_assert_code_400(kit_body)

def test_missing_token():
    invalid_kit_body = get_kit_name("TestKit")
    response = req.post_create_new_kit(invalid_kit_body, None)
    assert response.status_code == 401, "Error esperado 401 por falta de autenticación"

def test_get_new_user_token():
    token = get_new_user_token()
    assert token is not None, "Error: No se obtuvo el token correctamente"
