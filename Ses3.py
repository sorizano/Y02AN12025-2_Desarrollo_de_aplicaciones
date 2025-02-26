import streamlit as st

# Función para clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"
    
# Menú Lateral
st.sidebar.title("Menú de navegación")
opcion = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Clasificación de Puntajes"])

# Sección: Inicio
if opcion == "Inicio":
    st.title("Bienvenid@ a la aplicación") 

# Sección: Clasificación de Puntajes
elif opcion == "Clasificación de Puntajes":
    st.title("Clasificación de Puntajes")
    st.write("Ingese un puntaje y el sistema lo clasificará.")

    # Entrada de usuario
    puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

    # Botón para clasificar
    if st.button("Clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"El puntaje {puntaje} es clasificado como: {resultado}")