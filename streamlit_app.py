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
        st.image("assets/images/project.jpg", caption="Evaluacion de Hiperparametros y desempeño basado en diferentes metricas")
    st.write("Tecnologías utilizadas: Python, Pandas, Scikit-learn, etc.")

with st.expander("Proyecto 2"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Visión Artificial para imagenes Perro-Gato**")
        st.write("Proyecto enfocado en el desarrollo de un modelo de visión artificial para la clasificación de imagenes de perros y gatos, un caso tipico de clasificacion y vision artificial.")
    with col2:
        st.image("assets/images/perro_gato.jpg", caption="Imagen de referencia")
    st.write("Tecnologías utilizadas: Python, TensorFlow, OpenCV, Deep Learning")

with st.expander("Proyecto 3"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Gestion de Inventario Antioquia Ventas**")
        st.write("La persona encargada de logística tenia una necesidad de datos pues al exportar los inventarios y el saldo de sus productos estos estaban desorganizados y no seguían reglas de calidad de datos claras, por lo que se puso en contacto conmigo y me pidió crear algo que le permitiera procesar datos de forma eficaz y organizara su inventario de forma dinamica, por lo que desarrollé una Tuberia de datos que tomara cadenas de texto basadas en expresiones regulares y estableciera columnas y registros basados en el texto analisado por la expresion, dando como resultado datos limpios y analizables para la gestion de inventarios")
    with col2:
        st.image("assets/images/project2.jpg", caption="Tuberia Desplegada")
    st.write("Tecnologías utilizadas: Python, Pandas, Regex, ETL, Tuberia, Analitica de Datos, Calidad de Datos")

with st.expander("Proyecto 4"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Prediccion Energia Solar**")
        st.write("El proyecto tenia como objetivo fundamental el reconocimiento de variables esenciales para predicción del comportamiento de la generación de energía solar, para esto se compra una base de datos con un histórico de 5 años del comportamiento en las coordenadas cercanas a la UPB, con el objetivo de predecir el comportamiento de las variables climáticas durante 7 unidades de tiempo (días) a futuro, pues esta es la periodicidad que se encontró al desarrollar un modelo SARIMAX con el objetivo de saber cuanta energía podíamos generar de la radiación solar emitida durante los siguientes 7 días, de esta forma se gestionaban posibles desabastecimientos por este medio o se podría estimar ingresos generados por la comercialización de la energía restante a EPM")
    with col2:
        # Primero la imagen
        st.image("assets/images/project3.jpg", caption="Parametrizacion de Modelo SARIMAX")
        
        st.link_button(
            "📊 Ver Presentación en Canva",
            "https://www.canva.com/design/DAFgje-dpjA/EwNIhtXPUlkBNcMnKj33iA/edit?utm_content=DAFgje-dpjA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton",  # Reemplaza con tu URL real de Canva
            help="Haz clic para ver la presentación completa en Canva",
            type="primary",
            use_container_width=True  # Esto hace que el botón use el ancho completo disponible
        )
    st.write("Tecnologías utilizadas: Python, Pandas, Matplotlib, SARIMAX, etc.")

with st.expander("Proyecto 5"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("**Analisis de modelos Clustering por Diseño Factorial**")
        st.write("El objetivo del proyecto es comparar por medio de diseño factorial los métodos de agrupación K-Means y BIRCH, métodos que son útiles para hallar perfiles, grupos o patrones dentro de un conjunto de datos, generalmente, donde existan más de dos variables. El punto es evaluar el desempeño de ambos en un mismo conjunto de datos y basado en diferentes niveles de los factores existentes para medir la eficiencia del modelo seleccionado, dando como conclusión que el desempeño en comparación con el otro modelo es significativo para la eficiencia, siendo estadísticamente similar en ambos casos.")
    with col2:
        st.image("assets/images/project4.jpg", caption="Analisis de modelos Clustering por Diseño Factorial")

        st.link_button(
            "📄 Ver Documento PDF",
            "https://drive.google.com/file/d/19n2lTQtCTxcNx6upfV0Jc-3JWDwrIQEz/view?usp=sharing",
            help="Haz clic para ver el documento completo del proyecto",
            type="primary",
            use_container_width=True
        )
    st.write("Tecnologías utilizadas: R, Python, Scikit-learn, Pandas, Diseño Factorial, Análisis Estadístico")

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