
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Gatitos",
    page_icon=":sunglasses:",
    layout="wide"
)

# Título principal
st.title("Sitio Web de Gatitos 🐱")

# Insignia de contenido nuevo
st.badge("Contenido nuevo", color="green", icon=":material/done_outline:")

# Descripción inicial
st.write("Este es un sitio web sobre gatitos y otros animalitos adorables.")

# Barra de búsqueda
search_term = st.text_input("Buscar contenido (gatos, perros, gorditos, etc.):").lower().strip()

st.divider()
if search_term in ("", "perritos", "gatitos", "gorditos", "los gatitosy perritos son hermosos"):
    st.header("🐾 Sección 1 - Página 2", divider=True)
    col1, col2 = st.columns(2)
    col1.video("https://youtu.be/ENOyVvOmcZc?si=uU1LbyUeH5AbRJxk")
    col1.write("LOS GATIROS SON HERMOSOS")
    col1.write("AMAMOS A LOS GATOS Y PERROS")
    col1.write("los gatos más lindos son los gorditos")
    col2.write("Foto gatitos")
    col2.write("los perros son muy amables y cariñosos")
    col2.image("pr2.jpg", caption="Navegamos hacia el fin del mundo")
    col2.image("pr5.jpg")
    col1.image("ima6.jpg")
