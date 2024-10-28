import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi CV - Data Science",
    page_icon="👨‍💻",
    layout="wide"
)

# Encabezado principal
st.title("👨‍💻 Mi Portafolio de Data Science")

# Barra lateral con información personal
with st.sidebar:
    st.image("assets/images/profile.jpg", width=200)  # Ruta actualizada
    st.title("Información Personal")
    st.write("📧 tu@email.com")
    st.write("📱 Tu número de teléfono")
    st.write("📍 Tu ubicación")
    st.write("🔗 [LinkedIn](tu_perfil_linkedin)")
    st.write("🔗 [GitHub](tu_perfil_github)")

# Sección principal
st.header("Sobre mí")
st.write("""
    Aquí puedes escribir una breve introducción sobre ti, tu pasión por la ciencia de datos
    y tu experiencia como estudiante en este campo.
""")

# Experiencia académica
st.header("📚 Experiencia Académica")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Educación")
    st.write("**Universidad / Institución**")
    st.write("Carrera - Año")
    st.write("GPA / Logros destacados")

with col2:
    st.subheader("Certificaciones")
    st.write("- Certificación 1")
    st.write("- Certificación 2")

# Proyectos
st.header("🚀 Proyectos de Data Science")
with st.expander("Proyecto 1"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Nombre del Proyecto**")
        st.write("Descripción del proyecto")
    with col2:
        st.image("assets/images/project.jpg", caption="Proyecto 1")
    st.write("Tecnologías utilizadas: Python, Pandas, Scikit-learn, etc.")
    # Puedes añadir imágenes o gráficos de tus proyectos
    # st.image("proyecto1.jpg")

# Habilidades
st.header("🛠️ Habilidades Técnicas")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Lenguajes de Programación")
    st.write("- Python")
    st.write("- R")
    st.write("- SQL")

with col2:
    st.subheader("Herramientas y Frameworks")
    st.write("- Pandas")
    st.write("- Scikit-learn")
    st.write("- TensorFlow")

with col3:
    st.subheader("Soft Skills")
    st.write("- Trabajo en equipo")
    st.write("- Resolución de problemas")
    st.write("- Comunicación efectiva")

# Mi experiencia como estudiante
st.header("📝 Mi Viaje en Data Science")
st.write("""
    Aquí puedes compartir tu experiencia personal como estudiante de Data Science.
    Habla sobre:
    - Desafíos que has enfrentado
    - Lecciones aprendidas
    - Consejos para otros estudiantes
    - Tu visión del futuro en este campo
""")
