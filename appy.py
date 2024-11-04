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
    
# Llamar a la función para crear la tabla antes de hacer cualquier otra operación
create_table()

import sqlite3
import streamlit as st
import pandas as pd

st.image("./imagen.png")

# Código CSS para cambiar el color de fondo de la página y los botones
page_style = """
<style>
    /* Cambia el color de fondo de la página */
    .stApp {
        background-color: #1f93f9;
    }

    /* Cambia el estilo de los botones */
    div.stButton > button {
        background-color: #4CAF50; /* Color de fondo del botón */
        color: white; /* Color del texto del botón */
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }
    /* Cambia el color al pasar el mouse por encima */
    div.stButton > button:hover {
        background-color: #45a049;
    }
</style>
"""

# Aplica el CSS con st.markdown
st.markdown(page_style, unsafe_allow_html=True)

# Base de datos
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

# Llamar a la función para crear la tabla antes de hacer cualquier otra operación
create_table()

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
st.title('Plataforma para la Gestión y Publicación de proyectos  comunitarios y solidarios')

# Formulario para subir proyectos
st.header('Subí tu proyecto para facilitar su visibilizacion y la gestión de voluntarios')
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
