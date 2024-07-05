import pandas as pd
import streamlit as st

# Datos de muestra para el fixture de la Copa América 2024
fixture_data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Date': ['2024-07-02', '2024-07-05', '2024-07-08', '2024-07-03', '2024-07-06', '2024-07-09', '2024-07-04', '2024-07-07', '2024-07-10'],
    'Time': ['18:00', '20:00', '18:00', '18:00', '20:00', '18:00', '18:00', '20:00', '18:00'],
    'Team 1': ['Team A1', 'Team A2', 'Team A3', 'Team B1', 'Team B2', 'Team B3', 'Team C1', 'Team C2', 'Team C3'],
    'Team 2': ['Team A2', 'Team A3', 'Team A1', 'Team B2', 'Team B3', 'Team B1', 'Team C2', 'Team C3', 'Team C1'],
    'Venue': ['Stadium 1', 'Stadium 2', 'Stadium 1', 'Stadium 3', 'Stadium 4', 'Stadium 3', 'Stadium 5', 'Stadium 6', 'Stadium 5']
}

fixture_df = pd.DataFrame(fixture_data)

# Configuración de la aplicación Streamlit
st.title("Fixture de la Copa América 2024")
st.write("Aquí tienes el fixture actualizado de la Copa América 2024:")

# Mostrar el DataFrame en la aplicación
st.dataframe(fixture_df)

# Filtrar por grupo
group = st.selectbox("Selecciona un grupo", fixture_df['Group'].unique())
filtered_df = fixture_df[fixture_df['Group'] == group]
st.write(f"Partidos del Grupo {group}")
st.dataframe(filtered_df)
