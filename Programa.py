import pandas as pd
import streamlit as st
from datetime import datetime

# Cargar datos de la Copa América 2024
data = pd.read_csv('copa_americana_2024.csv')

# Crear una interfaz de usuario con Streamlit
st.title('Fixture Copa América 2024')
st.header('Partidos y Horarios')

# Mostrar los partidos y horarios
st.write('**Partidos y Horarios**')
st.table(data[['Equipo 1', 'Equipo 2', 'Fecha', 'Hora']])

# Crear un formulario para ingresar los resultados de los partidos
st.write('**Ingresar resultados de los partidos**')
form = st.form('partidos')
equipo1 = form.text_input('Equipo 1')
equipo2 = form.text_input('Equipo 2')
resultado = form.text_input('Resultado (1-0, 2-1, etc.)')
form.submit_button('Ingresar resultado')

# Procesar los resultados ingresados y actualizar la tabla
if form.button_clicked:
    resultado = resultado.split('-')
    equipo1_score = int(resultado[0])
    equipo2_score = int(resultado[1])
    data.loc[data['Equipo 1'] == equipo1, 'Puntos'] += equipo1_score
    data.loc[data['Equipo 2'] == equipo2, 'Puntos'] += equipo2_score
    st.write('**Actualizado**')

# Mostrar la clasificación actual
st.write('**Clasificación actual**')
st.table(data.groupby('Equipo')['Puntos'].sum().reset_index())

# Mostrar el fixture completo
st.write('**Fixture completo**')
st.table(data)