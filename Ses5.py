import streamlit as st

def main():
    st.title("Ejemplo de While y For en Streamlit")

    #Ejemplo de while
    st.subheader("Ejemplo de While")
    n = st.number_input("Ingresa un número para contar hasta 5:", min_value=0, max_value=5, step=1)
    contador = 0
    resultado_while = ""

    while contador <= n:
        resultado_while += f"{contador}"
        contador += 1
    st.write("Secuencia generada con while:", resultado_while)

    #Ejemplo de for
    st.subheader("Ejemplo con for")
    m = st.number_input("Ingrese un número para generar una secuencia:", min_value=1, max_value=10, step=1)
    resultado_for = "".join(f"{i} " for i in range(1, m +1))
    st.write("Secuencia generada con for:", resultado_for)

if __name__ == "__main__":
    main()