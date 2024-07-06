import streamlit as st
import requests
import os

# Asegúrate de que la clave de API esté definida en tu entorno antes de ejecutar el programa
api_key = os.getenv('OPENAI_KEY')
if not api_key:
    st.error("La clave de API no está configurada en el entorno. Por favor, define OPENAI_KEY en tu entorno.")
    st.stop()

api_url = 'https://api.openai.com/v1/chat/completions'

st.title('Generador de Campañas de Marketing para Restaurantes')
st.write('Proporciona la información solicitada para generar 30 copys personalizados para tus redes sociales.')

# Session state to manage input values
if 'giro' not in st.session_state:
    st.session_state.giro = ''
if 'mensaje' not in st.session_state:
    st.session_state.mensaje = ''

# Input fields without placeholders
giro = st.text_input('Giro del restaurante', st.session_state.giro)
mensaje = st.text_area('¿Qué se quiere comunicar este mes?', st.session_state.mensaje)

# Update session state with user input
st.session_state.giro = giro
st.session_state.mensaje = mensaje

if st.button('Generar Campaña'):
    # Configura los headers y el payload para la solicitud a la API de OpenAI
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un experto en marketing digital para restaurantes."},
            {"role": "user", "content": f"Genera 30 copys creativos para Facebook para un restaurante de {st.session_state.giro} que quiere comunicar {st.session_state.mensaje} este mes."}
        ],
        "max_tokens": 2000,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    # Realiza la solicitud a la API
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        copys = result['choices'][0]['message']['content'].strip().split('\n')
        for i, copy in enumerate(copys):
            st.write(f"{i + 1}. {copy}")
    else:
        st.error(f"Error al generar los copys. Código de estado: {response.status_code}. Detalles: {response.text}")
