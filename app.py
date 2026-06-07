import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header('Visualización del Mercado de Autos Usados')
# Leer los datos del archivo CSV
car_data = pd.read_csv('/Users/colibri/Desktop/Proy7/vehicles_env/vehicles_us.csv')

# Crear un botón en la aplicación Streamlit
hist_button = st.checkbox('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

build_disper = st.checkbox('Construir un grafico de dispersión')

if build_disper:
    st.write('Construyendo un grafico de dispersión...')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'])])
    st.plotly_chart(fig, use_container_width=True)