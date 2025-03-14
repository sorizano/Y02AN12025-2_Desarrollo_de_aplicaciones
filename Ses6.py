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

st.header("Clientes Registrados")
#obtener a los clientes
clientes = supabase.table("clientes").select("*").execute()
if clientes.data:
    for cliente in clientes.data:
        with st.expander (cliente["nombre"]):
            st.write(f"📧 {cliente['email']}")
            st.write(f"📞 {cliente['telefono']}")
            st.write(f"📅 Fecha Registro: {cliente['fecha_registro']}")

            #Botón para eliminar cliente
            if st.button(f"Eliminar {cliente['nombre']}", key=cliente["id"]):
                supabase.table("clientes").delete().eq("id", cliente["id"]).execute()
                st.success(f"{cliente['nombre']} eliminado correctamente")
                st.rerun()
            
            #Formulario para actualizar cliente
            st.subheader("Actualizar Cliente")
            nuevo_nombre = st.text_input("Nuevo Nombre", value=cliente["nombre"], key=f"nombre_{cliente['id']}")
            nuevo_email = st.text_input("Nuevo Email", value=cliente["email"], key=f"email_{cliente['id']}")
            nuevo_telefono = st.text_input("Nuevo Teléfono", value=cliente["telefono"], key=f"telefono_{cliente['id']}")

            if st.button("Actualizar", key=f"upd_{cliente['id']}"):
                supabase.table("clientes").update({
                    "nombre": nuevo_nombre,
                    "email": nuevo_email,
                    "telefono": nuevo_telefono
                }).eq("id", cliente["id"]).execute()

                st.success(f"{cliente['nombre']} actualizado correctamente")
                st.rerun()
        
else:
    st.info("No hay clientes registrados aún")