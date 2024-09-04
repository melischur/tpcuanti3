# tpcuanti3

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
