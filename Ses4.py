import streamlit as st

st.title("Estructuras de Control Repetitivas")

#Entrada del usuario para límite de bucle
limite = st.number_input("Ingrese un número límite para los bucles: ", min_value=1, step=1)

st.subheader("Bucle FOR")

for i in range(1, limite + 1):
    st.write(f"Iteración {i} con for")

st.subheader("Bucle While")
contador = 1
while contador <= limite:
    st.write(f"Intereación {contador} con while")
    contador += 1