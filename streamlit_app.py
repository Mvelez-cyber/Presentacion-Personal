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
    st.image("assets/images/profile.jpg", width=200)
    st.title("Información Personal")
    st.write("📧 mvelezsuarez04@email.com")
    st.write("📱 +57 320 788 96 32")
    st.write("📍 Envigado, Antioquia")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/miguel-velez-79703627a/)")
    st.write("🔗 [GitHub](https://github.com/Mvelez-cyber)")

# Sección principal
st.header("Sobre mí")
st.write("""
    Científico de Datos con una sólida base en diseño de experimentos y análisis estadístico avanzado, enfocado en aprovechar el potencial de los datos para tomar decisiones inteligentes. Tengo experiencia trabajando tanto con datos estructurados como no estructurados, desarrollando modelos de Machine Learning y generando insights valiosos. Además, soy ágil en metodologías de desarrollo como SCRUM y Kanban, lo que me permite adaptarme a diferentes equipos y proyectos.

He creado pipelines en Azure Data Factory, filtrado y perfilado datos, y trabajado en proyectos de analítica y desarrollo de insights usando Python. También cuento con experiencia en programación orientada a objetos en C# y un dominio robusto de SQL para manejar bases de datos y consultas complejas.
""")

# Experiencia académica
st.header("📚 Experiencia Académica")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Educación")
    st.write("**Universidad Pontificia Bolivariana**")
    st.write("Ingenieria en Ciencia De Datos / 2021 - 2024")

with col2:
    st.subheader("Certificaciones")
    st.write("- [Exploracion y Analisis de datos con Python](https://learn.microsoft.com/api/achievements/share/es-es/MiguelAngelVelezSuarez-8011/HAA7F628?sharingId=D9A14AF1504BC3F1)")
    st.write("- [Google Analytics Certification](https://skillshop.credential.net/b846f20e-5f50-4acd-8a32-7e85bf778958)")

# Proyectos
st.header("🚀 Proyectos de Data Science")
with st.expander("Proyecto 1"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Clasificacion Dengue**")
        st.write("El proyecto tenia como objetivo analizar datos de pacientes con dengue para predecir si un paciente tiene dengue con sintomas alarmantes para su estado de salud o no, facilitando la atencion de aquellos que presentaban sintomas de riesgo, usando un modelo de clasificación.")
    with col2:
        st.image("assets/images/project.jpg", caption="Proyecto 1")
    st.write("Tecnologías utilizadas: Python, Pandas, Scikit-learn, etc.")

with st.expander("Proyecto 2"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Visión Artificial para imagenes Perro-Gato**")
        st.write("Proyecto enfocado en el desarrollo de un modelo de visión artificial para la clasificación de imagenes de perros y gatos, un caso tipico de clasificacion y vision artificial.")
    with col2:
        st.image("assets/images/perro_gato.jpg", caption="Proyecto 2")
    st.write("Tecnologías utilizadas: Python, TensorFlow, OpenCV, Deep Learning")

# Habilidades
st.header("🛠️ Habilidades Técnicas")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Lenguajes de Programación")
    st.write("- Python")
    st.write("- C#")
    st.write("- SQL")

with col2:
    st.subheader("Herramientas y Frameworks")
    st.write("- Pandas")
    st.write("- Scikit-learn")
    st.write("- TensorFlow")
    st.write("- Azure Data Factory")
    st.write("- Streamlit")

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
