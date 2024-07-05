import streamlit as st
import requests

# Configura tu clave de API de OpenAI
api_key = 'TU_CLAVE_DE_API_DE_OPENAI'
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
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        copys = result['choices'][0]['text'].strip().split('\n')
        for i, copy in enumerate(copys):
            st.write(f"{i + 1}. {copy}")
    else:
        st.error("Error al generar los copys. Inténtalo de nuevo más tarde.")

