import pytest
import sender_stand_request as req
import data
from copy import copy

def get_kit_body(name):
    # Se hace una copia del diccionario original para no modificar data.kit_body
    current_body = copy(data.kit_body)
    current_body["name"] = name
    return current_body

def get_new_user_token():
    # Se envía la solicitud de creación de usuario usando data.user_body
    token = req.post_new_user(data.user_body)
    assert token is not None, "Error: No se pudo obtener el token de autenticación"
    return token

def post_new_client_kit(kit_body, auth_token):
    # Llama a la función definida en sender_stand_request para crear un kit
    return req.post_new_client_kit(kit_body, auth_token)

def positive_assert(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 201, f"Error en la creación del kit: {response.status_code}"
    assert response.json().get("name") == kit_body["name"], "El campo 'name' no coincide"

def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 400, f"Error esperado 400, pero se obtuvo: {response.status_code}"

def test_create_kit_valid_cases():
    valid_kit_bodies = [
        get_kit_body("a"),
        get_kit_body("El valor de prueba para esta comprobación será inferior a 51 caracteres"),
        get_kit_body("N%@*"),
        get_kit_body(" A Aaa "),
        get_kit_body("123")
    ]
    for kit_body in valid_kit_bodies:
        positive_assert(kit_body)

def test_create_kit_invalid_cases():
    invalid_kit_bodies = [
        get_kit_body(""),            # Nombre vacío
        get_kit_body("a" * 512),       # Excede el límite de 511 caracteres
        {},                          # Parámetro ausente
        get_kit_body(123)            # Tipo incorrecto
    ]
    for kit_body in invalid_kit_bodies:
        negative_assert_code_400(kit_body)

def test_missing_token():
    invalid_kit_body = get_kit_body("TestKit")
    response = post_new_client_kit(invalid_kit_body, None)
    assert response.status_code == 401, "Error esperado 401 por falta de autenticación"

def test_get_new_user_token():
    token = get_new_user_token()
    assert token is not None, "Error: No se obtuvo el token correctamente"
