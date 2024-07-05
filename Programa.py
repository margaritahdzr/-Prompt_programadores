import streamlit as st
import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API_DE_OPENAI'

st.title('Generador de Campañas de Marketing para Restaurantes')
st.write('Proporciona la información solicitada para generar 30 copys personalizados para tus redes sociales.')

# Entrada del usuario
giro = st.text_input('Giro del restaurante', 'Ej. Comida rápida, Sushi, Italiana, etc.')
mensaje = st.text_area('¿Qué se quiere comunicar este mes?', 'Ej. Nuevos platillos, Descuentos especiales, Eventos, etc.')

if st.button('Generar Campaña'):
    # Llama a la API de OpenAI para generar los copys
    prompt = f"Genera 30 copys creativos para Facebook para un restaurante de {giro} que quiere comunicar {mensaje} este mes."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    copys = response.choices[0].text.strip().split('\n')
    for i, copy in enumerate(copys):
        st.write(f"{i + 1}. {copy}")

