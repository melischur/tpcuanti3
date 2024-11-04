# tpcuanti3

import sqlite3

# Función para crear la tabla si no existe
def create_table():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
import streamlit as st

# Configura el color de fondo usando CSS personalizado
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Llamar a la función para crear la tabla antes de hacer cualquier otra operación
create_table()

import streamlit as st
import sqlite3
import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect('projects.db')
c = conn.cursor()

# Función para agregar proyectos
def add_project(title, description, author):
    c.execute('''
        INSERT INTO projects (title, description, author)
        VALUES (?, ?, ?)
    ''', (title, description, author))
    conn.commit()

# Función para obtener todos los proyectos
def get_projects():
    c.execute('SELECT title, description, author FROM projects')
    return c.fetchall()

# Interfaz de Streamlit
st.title('Proyectos de la Comunidad Universitaria')

# Formulario para subir proyectos
st.header('Subir un Proyecto')
title = st.text_input('Título')
description = st.text_area('Descripción')
author = st.text_input('Autor')

if st.button('Subir'):
    if title and description and author:
        add_project(title, description, author)
        st.success('Proyecto subido con éxito')
    else:
        st.error('Por favor, completa todos los campos')

# Mostrar proyectos
st.header('Ver Proyectos')
projects = get_projects()

for project in projects:
    st.subheader(project[0])
    st.write(f"**Descripción:** {project[1]}")
    st.write(f"**Autor:** {project[2]}")

# Cerrar la conexión
conn.close()
