import pandas as pd
import streamlit as st


def cargar_datos(ruta_archivo):
    """Cargar datos desde un archivo CSV."""
    datos = pd.read_csv(ruta_archivo, sep=';', encoding='latin1')
    return datos


def main():
    ruta_archivo = 'CSVPOO.csv'

    datos = cargar_datos(ruta_archivo)

    st.title('Informe de Enfermedades por País y Año')

    paises = datos['Country '].unique()
    seleccion_pais = st.selectbox('Selecciona un país:', paises)

    años = datos['Year'].unique()
    seleccion_año = st.selectbox('Selecciona un año:', años)

    st.title(f'Informe para {seleccion_pais} en el año {seleccion_año}')

    datos_seleccionados = datos[(datos['Country '] == seleccion_pais) & (datos['Year'] == seleccion_año)]

    alcohol_use_disorders = datos_seleccionados['Deaths - Alcohol use disorders - Age: All Ages (Number)'].values[0]

    cirrhosis = datos_seleccionados['Deaths - Cirrhosis and other chronic liver diseases - Age: All Ages (Number)'].values[0]
    diarrheal_diseases = datos_seleccionados['Deaths - Diarrheal diseases - Age: All Ages (Number)'].values[0]
    chronic_kidney_diseases = datos_seleccionados['Deaths - Chronic kidney disease - Age: All Ages (Number)'].values[0]

    st.write(f'País: {seleccion_pais}')
    st.write(f'Año: {seleccion_año}')

    st.write(f'Casos de trastorno por consumo de alcohol: {alcohol_use_disorders}')
    st.write(f'Casos de Cirrosis y otras enfermedades hepáticas crónicas: {cirrhosis}')
    st.write(f'Casos de enfermedades diarreicas: {diarrheal_diseases}')
    st.write(f'Casos de enfermedades crónicas del riñón: {chronic_kidney_diseases}')

    # Crear una tabla con los datos
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Trastorno por consumo de alcohol', 'Cirrosis y otras enfermedades hepáticas crónicas', 'Enfermedades diarreicas', 'Enfermedades crónicas del riñón'],
                                'Número de Casos': [alcohol_use_disorders, cirrhosis, diarrheal_diseases, chronic_kidney_diseases]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))


if __name__ == "__main__":
    main()
