import streamlit as st
from algoritmos import AlgortimosSecuenciales

st.title("Algortimos Secuenciales con POO en Streamlit")

#Entrada de usuario
numero = st.number_input("Ingrese un número entero positivo", min_value=1, value=5, step=1)

# Instanciamos la clase con el número ingresado
algoritmos = AlgortimosSecuenciales(numero)

#Botones para ejecutar los algoritmos secuenciales
if st.button("Calcular Suma de N números"):
    st.success(f"La suma de los primeros {numero} número es: {algoritmos.suma_n_numeros()}")