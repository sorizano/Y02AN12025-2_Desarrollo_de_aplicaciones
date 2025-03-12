import streamlit as st
from supabase import create_client, Client
import os

#configurar supabase
SUPABASE_URL = "https://ondncxfrkzerxndpzvjz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9uZG5jeGZya3plcnhuZHB6dmp6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU3NzksImV4cCI6MjA1NzMyMTc3OX0.i-CknD56TkjtSzTW8gp4Ulr0VldY28nL1J-FBHG8uyc"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Gestión de Clientes - CRUD con Supabase y Streamlit")

#Formulario para agregar cliente
st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Teléfono")

if st.button("Agregar Cliente"):
    if nombre and email:
        data = {"nombre": nombre, "email": email, "telefono":telefono}
        response = supabase.table("clientes").insert(data).execute()
        st.success("Cliente agregado correctamente")
    else:
        st.warning("Nombre y Email son obligatorios")