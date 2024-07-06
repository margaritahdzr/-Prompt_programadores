import streamlit as st
import requests
import os


def load_dotenv(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            # Eliminar espacios en blanco y saltos de línea
            line = line.strip()
            # Ignorar líneas vacías y comentarios
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key] = value


# Cargar variables de entorno desde el archivo .env
load_dotenv('.env')


# Acceder a la llave de ambiente desde el entorno del sistema
api_key = os.getenv('OPENAI_KEY')
api_url = 'https://api.openai.com/v1/completions'


st.title('Generador de Campañas de Marketing para Restaurantes')
st.write('Proporciona la información solicitada para generar 30 copys personalizados para tus redes sociales.')


# Entrada del usuario
giro = st.text_input('Giro del restaurante', 'Ej. Comida rápida, Sushi, Italiana, etc.')
mensaje = st.text_area('¿Qué se quiere comunicar este mes?', 'Ej. Nuevos platillos, Descuentos especiales, Eventos, etc.')


if st.button('Generar Campaña'):
    # Configura los headers y el payload para la solicitud a la API de OpenAI
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
   
    data = {
        "model": "text-davinci-003",
        "prompt": f"Genera 30 copys creativos para Facebook para un restaurante de {giro} que quiere comunicar {mensaje} este mes.",
        "max_tokens": 2000,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }


    # Realiza la solicitud a la API



