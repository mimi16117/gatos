import streamlit as st

st.set_page_config(
    page_title="Gatitos",
    page_icon=":sunglasses:"
    )

st.title("Bienvenido a mi sitio web de gatitos y perritos")
st.badge("Contenido nuevo", color="green", icon=":material/done_outline:")
st.write("Este es un sitio web sobre gatitos")

st.divider()

st.header("Gatito", divider=True)
col1, col2 = st.columns(2)
col1.video("https://youtu.be/hvi3J3yBRXI?si=BJVJZbSLtGCKCrPZ")
col1.write("LOS GATIROS Y PERRITOS SON HERMOSOS")
col2.write("Foto perritos y gatitos")
col1.write("AMAMOS A LOS GATOS Y PERROS")
col1.write("los gatos mas lindos son los gorditos")

col2.image("pr5.jpg", caption="Navegamos hacia el fin del mundo")
col2.image("copiasteve.jpg")

