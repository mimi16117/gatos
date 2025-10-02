# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="GATITOS Y PERRITOS",
    page_icon=":yellow_heart:",  # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

pg = st.navigation(["2TOFFEE.py", "tofpro2.py", "tofpro3.py","tofpro4.py"])
pg.run()