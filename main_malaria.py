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

    print(datos.columns)
    paises = datos['Country '].unique()
    seleccion_pais = st.selectbox('Selecciona un país:', paises)

    años = datos['Year'].unique()
    seleccion_año = st.selectbox('Selecciona un año:', años)

    st.title(f'Informe para {seleccion_pais} en el año {seleccion_año}')

    datos_seleccionados = datos[(datos['Country '] == seleccion_pais) & (datos['Year'] == seleccion_año)]

    malaria = datos_seleccionados['Deaths - Malaria -  Age: All Ages (Number)'].values[0]

    digestive_diseases = datos_seleccionados['Deaths - Digestive diseases - Age: All Ages (Number)'].values[0]
    diarrheal_diseases = datos_seleccionados['Deaths - Diarrheal diseases - Age: All Ages (Number)'].values[0]
    nutritional_diseases = datos_seleccionados['Deaths - Nutritional deficiencies - Age: All Ages (Number)'].values[0]

    st.write(f'País: {seleccion_pais}')
    st.write(f'Año: {seleccion_año}')

    st.write(f'Casos de Malaria: {malaria}')
    st.write(f'Casos de enfermedades digestivas: {digestive_diseases}')
    st.write(f'Casos de enfermedades diarreicas: {diarrheal_diseases}')
    st.write(f'Casos de deficiencias nutricionales: {nutritional_diseases}')



    # Crear una tabla con los datos
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Malaria', 'Enfermedades Digestivas', 'Enfermedades diarreicas', 'Deficiencias nutricionales'],
                                'Número de Casos': [malaria, digestive_diseases, diarrheal_diseases, nutritional_diseases]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))


if __name__ == "__main__":
    main()
