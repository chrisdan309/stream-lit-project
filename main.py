import pandas as pd
import streamlit as st


def cargar_datos(ruta_archivo):
    """Cargar datos desde un archivo CSV."""
    datos = pd.read_csv(ruta_archivo, sep=';', encoding='latin1')
    return datos

def Malaria(datos_seleccionados, seleccion_pais, seleccion_año):
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
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Malaria', 'Enfermedades Digestivas', 'Enfermedades diarreicas',
                                                       'Deficiencias nutricionales'],
                                'Número de Casos': [malaria, digestive_diseases, diarrheal_diseases,
                                                    nutritional_diseases]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))

def Drug(datos_seleccionados, seleccion_pais, seleccion_año):
    drug_use_disorders = datos_seleccionados['Deaths - Drug use disorders - Age: All Ages (Number)'].values[0]

    lower_respiratory_infections = \
    datos_seleccionados['Deaths - Lower respiratory infections - Age: All Ages (Number)'].values[0]
    cardiovascular_diseases = datos_seleccionados['Deaths - Cardiovascular diseases  - Age: All Ages (Number)'].values[
        0]
    tuberculosis = datos_seleccionados['Deaths - Tuberculosis -  Age: All Ages (Number)'].values[0]

    st.write(f'País: {seleccion_pais}')
    st.write(f'Año: {seleccion_año}')

    st.write(f'Casos de trastorno por uso de drogas: {drug_use_disorders}')
    st.write(f'Casos de infecciones de las vías respiratorias inferiores: {lower_respiratory_infections}')
    st.write(f'Casos de enfermedades cardiovasculares: {cardiovascular_diseases}')
    st.write(f'Casos de tuberculosis: {tuberculosis}')

    # Crear una tabla con los datos
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Trastorno por uso de drogas',
                                                       'Infecciones de las vías respiratorias inferiores',
                                                       'Enfermedades cardiovasculares', 'Tuberculosis'],
                                'Número de Casos': [drug_use_disorders, lower_respiratory_infections,
                                                    cardiovascular_diseases, tuberculosis]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))

def Alcohol(datos_seleccionados, seleccion_pais, seleccion_año):
    alcohol_use_disorders = datos_seleccionados['Deaths - Alcohol use disorders - Age: All Ages (Number)'].values[0]

    cirrhosis = \
    datos_seleccionados['Deaths - Cirrhosis and other chronic liver diseases - Age: All Ages (Number)'].values[0]
    diarrheal_diseases = datos_seleccionados['Deaths - Diarrheal diseases - Age: All Ages (Number)'].values[0]
    chronic_kidney_diseases = datos_seleccionados['Deaths - Chronic kidney disease - Age: All Ages (Number)'].values[0]

    st.write(f'País: {seleccion_pais}')
    st.write(f'Año: {seleccion_año}')

    st.write(f'Casos de trastorno por consumo de alcohol: {alcohol_use_disorders}')
    st.write(f'Casos de Cirrosis y otras enfermedades hepáticas crónicas: {cirrhosis}')
    st.write(f'Casos de enfermedades diarreicas: {diarrheal_diseases}')
    st.write(f'Casos de enfermedades crónicas del riñón: {chronic_kidney_diseases}')

    # Crear una tabla con los datos
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Trastorno por consumo de alcohol',
                                                       'Cirrosis y otras enfermedades hepáticas crónicas',
                                                       'Enfermedades diarreicas', 'Enfermedades crónicas del riñón'],
                                'Número de Casos': [alcohol_use_disorders, cirrhosis, diarrheal_diseases,
                                                    chronic_kidney_diseases]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))

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

    tab1, tab2, tab3 = st.tabs(["Malaria", "Drug", "Alcohol"])

    with tab1:
        Malaria(datos_seleccionados, seleccion_pais, seleccion_año)

    with tab2:
        Drug(datos_seleccionados, seleccion_pais, seleccion_año)

    with tab3:
        Alcohol(datos_seleccionados, seleccion_pais, seleccion_año) 

if __name__ == "__main__":
    main()