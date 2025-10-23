
# --- REQUERIMIENTO 2 & 8: Configuración de la Página de Inicio (Icono y Título) ---
st.set_page_config(
    page_title="Gol-Ego: El Árbitro Virtual de Handball",
    page_icon="./assets/logo_golego.png",
    layout="wide"
)

# --- REQUERIMIENTO 3: Ruta a la Imagen del Logo ---
LOGO_PATH = "./assets/logo_golego.png"

# ------------------------------------------------------------------------------
# --- SECCIÓN HOME PAGE (REQUERIMIENTO 1 & 6) ---
# ------------------------------------------------------------------------------

st.image(LOGO_PATH, width=150)
st.title("⚽ GOL-EGO: Tu Guía Rápida de Reglas de Handball")
st.markdown("---")


## A. Problema a Resolver (REQUERIMIENTO 1.a)
st.header("1. El Problema: Confusión en la Cancha 🤯")
st.write("""
El balonmano (handball) es un deporte rápido y dinámico, pero sus reglas específicas 
(como el límite de pasos, el tiempo de posesión y las sanciones) a menudo confunden 
a jugadores novatos, padres, entrenadores en formación y árbitros principiantes. 
Una decisión equivocada puede cambiar el curso de un partido y generar frustración.
**Necesitamos una referencia rápida e interactiva, ¡no un manual de 300 páginas!**
""")

st.markdown("---")

## B. Usuario Objetivo (REQUERIMIENTO 1.b)
st.header("2. Nuestro Usuario: El Novato Entusiasta 🧑‍🎓")
st.subheader("Perfil: Juan, el Futuro Árbitro")
st.write("""
- **Edad:** 16 años.
- **Ubicación:** Estudiante de educación física que recién comienza a arbitrar partidos de ligas escolares.
- **Estilo de Vida:** Activo, siempre con su teléfono para revisar información deportiva.
- **Problema:** En el calor del juego, olvida la señal de arbitraje correcta o duda si la falta amerita un 'Golpe Franco' o una 'Exclusión'.
""")

st.markdown("---")

## C. Solución de la Aplicación (REQUERIMIENTO 1.c)
st.header("3. La Solución: Gol-Ego al Rescate 🚀")
st.write("""
**Gol-Ego** es una aplicación web intuitiva desarrollada en Python y Streamlit que sirve 
como un **árbitro virtual de bolsillo**. Permite al usuario simular situaciones de juego 
mediante entradas sencillas (sliders y menús) y devuelve instantáneamente la decisión 
reglamentaria y la señal de arbitraje visual correcta.

*¡Nunca más dudarás de la regla de los 3 pasos!*
""")



3. pages/1_Simulador_Arbitral.py (App Principal)
Esta es la sección interactiva central (Requerimiento 4).
Python
import streamlit as st

# --- REQUERIMIENTO 8: Widgets y Lógica Principal ---

st.title("🤾‍♂️ Simulador de Decisión Arbitral")
st.subheader("Ingresa la situación y Gol-Ego te da la decisión.")

# ----------------- Datos de Sanciones y Señales (REQUERIMIENTO 3) -----------------
# Diccionario para mapear la decisión a la imagen de la señal
SEÑALES = {
    "Golpe Franco": "./assets/senial_golpefranco.png",
    "Exclusión (2 min)": "./assets/senial_exclusion.png",
    "Lanzamiento de 7 metros": "./assets/senial_7metros.png",
    "Continuar Juego": "./assets/logo_golego.png" # Usamos el logo para 'continuar'
}

# ----------------- ENTRADAS DEL USUARIO (WIDGETS) -----------------

with st.sidebar:
    st.header("Opciones de Simulación")
    
    # Widget 1: Selectbox para la Categoría de la Falta
    tipo_falta = st.selectbox(
        "Categoría de la Falta",
        ["Pasos Ilegales", "Bote Ilegal", "Área de 6 metros", "Falta Agresiva"]
    )

st.markdown("---")

# ----------------- LÓGICA DE LA APLICACIÓN (REQUERIMIENTO 4) -----------------

decision = None
regla = None
senial_clave = None

if tipo_falta == "Pasos Ilegales":
    # Widget 2: Slider para el número de pasos
    num_pasos = st.slider("¿Cuántos pasos dio el jugador con el balón en la mano?", 1, 6, 3)
    
    if num_pasos > 3:
        decision = "FALTA: Pasos Ilegales."
        regla = "El reglamento solo permite un máximo de 3 pasos antes o después de botar."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "El jugador dio 3 o menos pasos. La jugada puede continuar."
        senial_clave = "Continuar Juego"
        
elif tipo_falta == "Bote Ilegal":
    # Widget 3: Checkbox
    rebote = st.checkbox("¿El jugador realizó un doble bote (botó, agarró con dos manos y volvió a botar)?")
    
    if rebote:
        decision = "FALTA: Doble Bote Ilegal."
        regla = "Una vez que el jugador detiene el bote agarrando el balón con ambas manos, no puede volver a botar. Debe pasar o lanzar."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "El bote fue reglamentario."
        senial_clave = "Continuar Juego"

elif tipo_falta == "Área de 6 metros":
    # Widget 4: Radio para la ubicación de la falta
    ubicacion = st.radio(
        "¿Dónde pisó el atacante?",
        ["Fuera del área (válido)", "Línea del área (válido)", "Dentro del área (invasión)"]
    )
    
    if ubicacion == "Dentro del área (invasión)":
        decision = "FALTA: Invasión del Área de Portería."
        regla = "Un jugador de campo no puede pisar el área de 6 metros. El portero es el único autorizado."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "Es válido pisar la línea del área (considerado fuera) o no pisarla."
        senial_clave = "Continuar Juego"

elif tipo_falta == "Falta Agresiva":
    # Widget 5: Selectbox para el nivel de agresión
    agresion = st.selectbox(
        "Nivel de Contacto",
        ["Forcejeo normal", "Sujeción/Empujón repetitivo", "Contacto directo a la cabeza/cuello"]
    )
    
    if agresion == "Contacto directo a la cabeza/cuello":
        decision = "SANCIÓN GRAVE: Exclusión."
        regla = "Todo contacto con riesgo de lesión o falta intencional requiere al menos dos minutos de exclusión."
        senial_clave = "Exclusión (2 min)"
    elif agresion == "Sujeción/Empujón repetitivo":
        decision = "SANCIÓN LEVE: Amonestación (Tarjeta Amarilla)."
        regla = "Señala una conducta incorrecta que podría escalar."
        senial_clave = "Golpe Franco" # O se podría usar una señal de amonestación si se tuviera la imagen
    else:
        decision = "Juego Válido."
        regla = "El forcejeo es parte del juego. No se requiere sanción."
        senial_clave = "Continuar Juego"


# ----------------- RESULTADO DE LA APLICACIÓN -----------------

st.markdown("## 🎯 Resultado y Decisión")
if decision:
    if "FALTA" in decision or "SANCIÓN" in decision:
        st.error(f"🚨 **DECISIÓN ARBITRAL:** {decision}")
        st.info(f"**REGLA APLICADA:** {regla}")
    else:
        st.success(f"✅ **DECISIÓN ARBITRAL:** {decision}")
        st.info(f"**REGLA APLICADA:** {regla}")
        
    st.markdown("---")
    
    st.markdown(f"### Señal de Arbitraje: {senial_clave}")
    
    # Muestra la imagen de la señal correspondiente
    if senial_clave in SEÑALES:
        st.image(SEÑALES[senial_clave], caption=senial_clave, width=250)



4. pages/2_Reglas_y_Seniales.py (Referencia Visual)
Python
import streamlit as st

st.title("📖 Referencia Rápida: Cancha y Señales")
st.markdown("---")

# ----------------- Reglas con Expansión y Contenido Multimedia -----------------

st.header("1. El Campo de Juego 🏟️")
st.info("Conoce las zonas clave para entender las faltas de invasión.")
st.image("./assets/cancha_handball.jpg", caption="Diagrama Oficial de la Cancha de Handball", use_column_width=True)

st.markdown("---")

st.header("2. Sanciones y Señales ✋")
st.info("Identifica visualmente la señal correcta que debe hacer el árbitro.")

# Uso de st.expander para organizar la información (REQUERIMIENTO 8)
with st.expander("Señal de Golpe Franco"):
    st.write("""
    **¿Cuándo se usa?** Es la sanción más común. Se usa para faltas menores o reglas técnicas no cumplidas (ej. pasos ilegales, doble bote, entrar al área).
    """)
    st.image("./assets/senial_golpefranco.png", width=200, caption="Golpe Franco")

with st.expander("Señal de Lanzamiento de 7 Metros"):
    st.write("""
    **¿Cuándo se usa?** Similar a un penal. Se sanciona cuando una clara ocasión de gol es impedida ilegalmente por la defensa o el portero.
    """)
    st.image("./assets/senial_7metros.png", width=200, caption="Lanzamiento de 7 metros")

with st.expander("Señal de Exclusión (2 minutos)"):
    st.write("""
    **¿Cuándo se usa?** Para faltas más graves, contacto ilegal repetido, o conducta antideportiva. El jugador debe abandonar el campo por 2 minutos.
    """)
    st.image("./assets/senial_exclusion.png", width=200, caption="Exclusión de 2 minutos")

# Nota: Puedes agregar videos cortos de YouTube sobre las reglas usando st.video()
# st.header("3. Video Demostrativo")
# st.video("URL_DE_UN_VIDEO_SOBRE_PASOS_ILEGALES")



5. pages/3_Contacto.py (Contacto)
Python
import streamlit as st

# ----------------- SECCIÓN CONTACTO (REQUERIMIENTO 6) -----------------

st.title("📞 Equipo de Desarrollo y Contacto")
st.markdown("---")

st.header("Integrantes del Equipo de Gol-Ego")

st.markdown("""
| Rol | Nombre del Integrante |
| :--- | :--- |
| 🧑‍💻 **Developer** | [Nombre del Developer] |
| 🧠 **Product Manager** | [Nombre del Product Manager] |
| 👔 **CEO** | [Nombre del CEO] |
""")

st.subheader("Información del Curso")
st.write(f"""
- **Unidad:** 4. Elaboración de apps para dispositivos electrónicos móviles
- **Curso:** [Tu Curso/Asignatura]
- **Objetivo de Aprendizaje:** 5. Desarrollar aplicaciones para dispositivos móviles...
""")

st.markdown("---")
st.balloons()


 