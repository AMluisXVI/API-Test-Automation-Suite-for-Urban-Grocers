import requests
import configuration
import data


# Función para crear un nuevo usuario y obtener el token de autenticación
def post_new_user():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers
    )

    if response.status_code == 201:
        return response.json().get("token")
    else:
        print(f"⚠️ Error al crear usuario: {response.status_code} - {response.text}")
        return None


# Función para crear un nuevo kit de producto
def post_new_client_kit(kit_body, auth_token):
    if not auth_token:
        raise ValueError("❌ No se proporcionó un token de autenticación. La solicitud no puede ejecutarse.")

    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )

    return response
