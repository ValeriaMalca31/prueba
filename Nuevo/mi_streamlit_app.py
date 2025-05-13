import streamlit as st

st.title("Hola, Streamlit 👋")
st.write("¡Esta es mi primera app con Streamlit!")

import streamlit as st
import pandas as pd

st.title("Ejemplo interactivo")

name = st.text_input("¿Cómo te llamas?")
if name:
    st.write(f"¡Hola, {name}!")

if st.button("Mostrar tabla"):
    data = pd.DataFrame({
        "Columna 1": [1, 2, 3],
        "Columna 2": [4, 5, 6]
    })
    st.write(data)
