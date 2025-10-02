if search_term  in ("gatos", "gatitos", "gorditos", "pagina 2", "los gatiros son hermosos"):
    search_term = "gatitos"
    st.header("🐾 Sección 1 - Página 2", divider=True)
    col1, col2 = st.columns(2)
    col1.video("https://youtu.be/hvi3J3yBRXI?si=BJVJZbSLtGCKCrPZ")
    col1.write("LOS GATIROS SON HERMOSOS")
    col1.write("AMAMOS A LOS GATOS")
    col1.write("los gatos más lindos son los gorditos")
    col2.write("Foto gatitos")
    col2.write("los perros son muy amables y cariñosos")
    col2.image("OIP(6).jpg", caption="Navegamos hacia el fin del mundo")
    col2.image("OIP(5).jpg")
    col1.image("ima6.jpg")






