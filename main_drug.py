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

    drug_use_disorders = datos_seleccionados['Deaths - Drug use disorders - Age: All Ages (Number)'].values[0]

    lower_respiratory_infections = datos_seleccionados['Deaths - Lower respiratory infections - Age: All Ages (Number)'].values[0]
    cardiovascular_diseases = datos_seleccionados['Deaths - Cardiovascular diseases  - Age: All Ages (Number)'].values[0]
    tuberculosis = datos_seleccionados['Deaths - Tuberculosis -  Age: All Ages (Number)'].values[0]

    st.write(f'País: {seleccion_pais}')
    st.write(f'Año: {seleccion_año}')

    st.write(f'Casos de trastorno por uso de drogas: {drug_use_disorders}')
    st.write(f'Casos de infecciones de las vías respiratorias inferiores: {lower_respiratory_infections}')
    st.write(f'Casos de enfermedades cardiovasculares: {cardiovascular_diseases}')
    st.write(f'Casos de tuberculosis: {tuberculosis}')

    # Crear una tabla con los datos
    datos_tabla = pd.DataFrame({'Tipo de Enfermedad': ['Trastorno por uso de drogas', 'Infecciones de las vías respiratorias inferiores', 'Enfermedades cardiovasculares', 'Tuberculosis'],
                                'Número de Casos': [drug_use_disorders, lower_respiratory_infections, cardiovascular_diseases, tuberculosis]})
    st.write("Tabla de Datos:")
    st.write(datos_tabla)

    # Crear un gráfico de barras
    st.bar_chart(datos_tabla.set_index('Tipo de Enfermedad'))


if __name__ == "__main__":
    main()
