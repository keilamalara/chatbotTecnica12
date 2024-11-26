import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import streamlit.components.v1 as components

# Título del chatbot
st.title('El Instituto Superior de Formación Técnica Nº 12')

# Menú de opciones
opcion = st.selectbox("Selecciona una opción:", 
                      ["Técnicaturas", 
                       "Instituto", 
                       "Encuesta personal", 
                       "Test vocacional", 
                       "Ingreso"], 
                      key='menu_opcion')

# Sección de Técnicaturas

tecnicatura = None
if opcion == "Técnicaturas":
    st.subheader("Información sobre Técnicaturas")
    tecnicatura = st.selectbox(
        "Elige la tecnicatura que te interesa:", 
        [
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos", 
            "Tecnicatura Superior en Análisis de Sistemas", 
            "Tecnicatura Superior en Desarrollo de Software", 
            "Tecnicatura Superior en Administración Contable", 
            "Tecnicatura Superior en Administración Financiera", 
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo", 
            "Tecnicatura Superior en Ceremonial y Protocolo", 
            "Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial"
        ],
        key='tecnicatura_opcion'
    )

    if tecnicatura == "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos":
        st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
        
        # Pestañas para Internet de las Cosas y Sistemas Embebidos
        tab1, tab2, tab3, tab4 = st.tabs(["Materias", "Horarios", "Descripción", "Competencias"])

        with tab1:
            st.write("**Materias Primer Año**")
            st.write("1. Lógica Computacional - 4 horas por semana")
            st.write("2. Administración y Gestión de Base de Datos - 4 horas por semana")
            st.write("3. Elementos de Análisis Matemático - 4 horas por semana")
            st.write("4. Estadística y Probabilidades para Gestión de Datos - 4 horas por semana")
            st.write("5. Inglés I - 2 horas por semana")
            st.write("6. Inglés II - 2 horas por semana")
            st.write("7. Práctica Profesionalizante I: Aproximación al Campo Laboral - 4 horas por semana")
            st.write("8. Comunicación - 2 horas por semana")
        
        with tab2:
            st.write("**Horarios**")
            st.write("TOTAL ANUAL DE HORAS CURSADAS: 512 horas. Lunes a Viernes - 8:00 a 12:00 hs")
        
        with tab3:
            st.write("**Descripción de la Materia**")
            st.write("La Tecnicatura Superior en IoT y Sistemas Embebidos se enfoca en la modernización de procesos mediante la Internet de las Cosas (IoT), que permite conectar dispositivos a Internet para obtener y manipular grandes volúmenes de datos. Esta especialización es altamente demandada para la actualización de plantas de fabricación y otros entornos productivos, facilitando la toma de decisiones en tiempo real a través del manejo seguro y eficiente de la información.")
        
        with tab4:
            st.write("**Competencias**")
            st.write("La/el Técnica/o Superior en Internet de las Cosas y Sistemas Embebidos estará capacitada/o para definir, diseñar y gestionar proyectos tecnológicos con el uso de plataformas profesionales y avanzadas, creando redes de interconexión de los objetos con Internet.")
            st.write("1. Proyectar, dirigir y ejecutar sistemas de IoT y sistemas embebidos en hardware, firmware y software.")
            st.write("2. Enseñar conocimientos tecnológicos y científicos relacionados con IoT y sistemas embebidos.")
            st.write("3. Aplicar normas de calidad, seguridad, legales y de protección del medio ambiente.")
            st.write("4. Diseñar, rediseñar, programar e implementar sistemas embebidos.")

    if tecnicatura == "Tecnicatura Superior en Desarrollo de Software":
        st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
        
        # Pestañas para Desarrollo de Software
        tab1, tab2, tab3, tab4 = st.tabs(["Materias", "Horarios", "Descripción", "Competencias"])

        with tab1:
            st.write("**Materias Primer Año**")
            st.write("1. Programación - 4 horas por semana")
            st.write("2. Bases de Datos - 4 horas por semana")
            st.write("3. Matemáticas Discretas - 4 horas por semana")
            st.write("4. Metodologías Ágiles - 4 horas por semana")
            st.write("5. Práctica Profesionalizante I - 4 horas por semana")
        
        with tab2:
            st.write("**Horarios**")
            st.write("TOTAL ANUAL DE HORAS CURSADAS: 512 horas. Lunes a Viernes - 8:00 a 12:00 hs")
        
        with tab3:
            st.write("**Descripción de la Materia**")
            st.write("La Tecnicatura Superior en Desarrollo de Software se centra en formar profesionales capaces de crear soluciones de software innovadoras y eficientes.")
        
        with tab4:
            st.write("**Competencias**")
            st.write("Los egresados estarán capacitados para diseñar, implementar y gestionar proyectos de software, con habilidades en análisis y resolución de problemas.")


if tecnicatura == "Tecnicatura Superior en Ceremonial y Protocolo":
    st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
        
    # Pestañas para Ceremonial y Protocolo
    tab1, tab2, tab3, tab4 = st.tabs(["Materias", "Horarios", "Descripción", "Competencias"])

    with tab1:
        st.write("**Materias Primer Año**")
        st.write("1. Inglés I")
        st.write("2. Informática")
        st.write("3. Historia de las Instituciones Argentinas I")
        st.write("4. Antropología Cultural")
        st.write("5. Psicología de Grupos e Institución")
        st.write("6. Portugués I")
        st.write("7. Ceremonial y Protocolo I")
        st.write("8. Redacción Formal")
        st.write("9. Comportamiento Social")
        st.write("10. Práctica Profesional I")
        
    with tab2:
        st.write("**Horarios**")
        st.write("Lunes a Viernes - 18:00 a 21:30 hs")
        st.write("Sábados - 8:00 a 15:00 hs")
        st.write("Prácticas profesionalizantes en días y horarios a coordinar.")
        
    with tab3:
        st.write("**Descripción de la Materia**")
        st.write("El Área de Ceremonial y Protocolo se ocupa de diseñar, organizar e implementar la logística y el desarrollo de actos y eventos institucionales. Además, interviene en el diseño, selección, adquisición y preparación de objetos institucionales tales como presentes. También se encarga del cuidado, tutela y colocación de símbolos patrios, cartelería y elementos de ornato. Se ocupa además del asesoramiento a funcionarios y públicos de la universidad en materia de ceremonial y protocolo y de la comunicación protocolar con los distintos públicos.")
        
    with tab4:
        st.write("**Competencias**")
        st.write("1. Organizar, coordinar, planificar y supervisar todos los actos, recepciones y ceremonias de la organización.")
        st.write("2. Asistir, acompañar y asesorar a los titulares y representantes de la organización.")
        st.write("3. Elaborar el ordenamiento y las precedencias de la repartición, empresa o institución.")
        st.write("4. Capacitar al personal para el desarrollo de encuentros sociales.")
        st.write("5. Asesorar con respecto a la imagen.")
        st.write("6. Realizar y registrar las comunicaciones sociales de la organización.")

if tecnicatura == "Tecnicatura Superior en Higiene y Seguridad en el Trabajo":
        st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
        
        # Pestañas para Higiene y Seguridad
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Materias", "Duración", "Habilidades y Competencias", "Salidas Laborales", "Apoyo a Estudiantes"])

        with tab1:
            st.write("**Materias Cursadas**")
            st.write("1. Comunicación y administración de medios")
            st.write("2. Higiene laboral y medio ambiente")
            st.write("3. Medicina del trabajo")
            st.write("4. Ergonomía")
            st.write("5. Estadística")
        
        with tab2:
            st.write("**Duración del Programa**")
            st.write("La carga horaria total es de 640 horas.")
        
        with tab3:
            st.write("**Habilidades y Competencias**")
            st.write("Se desarrollan en diseño y gestión de programas de seguridad, identificación y control de riesgos, y comunicación efectiva.")
        
        with tab4:
            st.write("**Salidas Laborales**")
            st.write("Incluyen planificación, organización y gestión de actividades de seguridad e higiene.")
            st.write("Las instituciones contratantes incluyen empresas industriales, de construcción, servicios de salud y organismos gubernamentales.")
        
        with tab5:
            st.write("**Prácticas Profesionales**")
            st.write("Están incluidas en el plan de estudios.")
            st.write("Oportunidades de especialización: Los egresados pueden optar por especializaciones en seguridad e higiene.")
            st.write("Apoyo a estudiantes: Talleres de desarrollo profesional, ferias de empleo y asesoramiento para la inserción laboral.")


if tecnicatura == "Tecnicatura Superior en Análisis de Sistemas":
    st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")
    
    # Pestañas para Análisis de Sistemas
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
        ["Definición", "Competencias", "Funciones", "Estructura Curricular", "Materias Primer Año", 
         "Beneficios", "Áreas de Desempeño", "Habilitaciones", "Requisitos de Ingreso", 
         "Certificaciones en Inglés"]
    )

    with tab1:
        st.write("**Definición del Área**")
        st.write("El análisis de sistemas es un área de la informática que se ocupa de sistemas informáticos, caracterizados por ser un conjunto de procedimientos que facilitan la administración, recolección, procesamiento y distribución de información.")

    with tab2:
        st.write("**Competencias del Analista de Sistemas**")
        st.write("El analista está capacitado para planificar y gestionar proyectos de desarrollo, diagnosticar problemas y diseñar soluciones informáticas.")

    with tab3:
        st.write("**Funciones del Técnico Superior**")
        st.write("Incluyen la planificación y evaluación de proyectos de sistemas de información, diagnóstico de problemas organizacionales, y gestión de la operación y mantenimiento de sistemas.")

    with tab4:
        st.write("**Estructura Curricular**")
        st.write("Se organiza en cuatro campos: Formación General, Formación de Fundamento, Formación Técnica Específica y Prácticas Profesionalizantes.")

    with tab5:
        st.write("**Materias del Primer Año**")
        st.write("1. Inglés I")
        st.write("2. Ciencia, Tecnología y Sociedad")
        st.write("3. Análisis Matemático I")
        st.write("4. Álgebra")
        st.write("5. Algoritmos y Estructuras de Datos I")
        st.write("6. Sistemas y Organizaciones")
        st.write("7. Arquitectura de Computadores")
        st.write("8. Prácticas Profesionalizantes I")

    with tab6:
        st.write("**Beneficios para las Organizaciones**")
        st.write("Permite optimizar procedimientos, automatizar sistemas de información, mejorar controles y ajustar costos.")

    with tab7:
        st.write("**Áreas de Desempeño**")
        st.write("Puede desempeñarse en cualquier organización que requiera análisis y diseño de sistemas de información, así como en consultorías.")

    with tab8:
        st.write("**Habilitaciones Profesionales**")
        st.write("Puede analizar, diseñar, implementar y verificar sistemas de información, exceptuando sistemas críticos para la seguridad.")

    with tab9:
        st.write("**Requisitos de Ingreso**")
        st.write("Se requiere haber completado la Educación Secundaria.")

    with tab10:
        st.write("**Certificaciones en Inglés**")
        st.write("Al finalizar, los estudiantes pueden obtener el certificado de capacitación laboral Inglés Nivel 3 B1.")

if tecnicatura == "Tecnicatura Superior en Administración Contable":
    st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")

    # Pestañas para Administración Contable
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
        ["Habilidades", "Tecnologías", "Conocimientos", "Duración", "Salidas Laborales", 
         "Objetivo", "Prácticas", "Formación en Software", "Proyectos", "Importancia"]
    )

    with tab1:
        st.write("**Habilidades Desarrolladas**")
        st.write("Se desarrollan habilidades técnicas específicas y competencias en procesos y funciones administrativas.")

    with tab2:
        st.write("**Tecnologías Digitales Utilizadas**")
        st.write("Se utilizan tecnologías digitales específicas del área de administración y finanzas.")

    with tab3:
        st.write("**Conocimientos Abordados**")
        st.write("Incluyen administración, finanzas, matemáticas financieras, costos y planificación.")

    with tab4:
        st.write("**Duración de la Carrera**")
        st.write("Es de 3 años, con una carga horaria total de 1824 horas anuales.")

    with tab5:
        st.write("**Salidas Laborales**")
        st.write("Incluyen administración de recursos humanos, consultoría, diseño y ejecución de proyectos, asesoría en comercio exterior y gestión de costos.")

    with tab6:
        st.write("**Objetivo de la Carrera**")
        st.write("Formar profesionales en gestión administrativa y contable para diversos sectores económicos.")

    with tab7:
        st.write("**Prácticas Profesionalizantes**")
        st.write("Se realizan para aplicar conocimientos en entornos laborales reales.")

    with tab8:
        st.write("**Formación en Software Contable**")
        st.write("Incluye capacitación en herramientas digitales y software contable.")

    with tab9:
        st.write("**Proyectos en Prácticas**")
        st.write("Participación en proyectos de análisis financiero, elaboración de presupuestos y auditorías.")

    with tab10:
        st.write("**Importancia del Análisis Financiero**")
        st.write("Es crucial para evaluar la salud económica de una organización y tomar decisiones informadas.")





if tecnicatura == "Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial":
    st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")

    # Pestañas para Ciencia de Datos e Inteligencia Artificial
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Horarios", "Asignaturas", "Competencias", "Estructura del Plan", "Equivalencias", "Prácticas"]
    )

    with tab1:
        st.write("**Horarios de Clases**")
        st.write("Las clases se organizan en un total de 16 semanas de cursada por cuatrimestre, "
                  "con una carga horaria total de 1408 horas. Las sesiones pueden variar, "
                  "pero generalmente se distribuyen a lo largo de la semana, incluyendo clases teóricas y prácticas.")

    with tab2:
        st.write("**Asignaturas del Plan de Estudio**")
        st.write("El plan de estudio incluye asignaturas como Seminario de Actualización, "
                  "Técnicas de Procesamiento Digital de Imágenes, y diversas materias relacionadas "
                  "con la inteligencia artificial y el análisis de datos. "
                  "Cada asignatura está diseñada para complementar y profundizar los conocimientos adquiridos.")

    with tab3:
        st.write("**Competencias Desarrolladas**")
        st.write("Los estudiantes desarrollarán competencias como el diseño de sistemas de inteligencia "
                  "artificial, procesamiento de imágenes, análisis de datos, y habilidades de trabajo en equipo. "
                  "También se enfatiza la importancia de la reflexión sobre el rol profesional y la interacción "
                  "en equipos de trabajo.")

    with tab4:
        st.write("**Estructura del Plan de Estudio**")
        st.write("El plan de estudio está estructurado en módulos que combinan teoría y práctica. "
                  "Incluye prácticas profesionalizantes desde el inicio de la carrera, "
                  "con un total de 64 horas en los dos primeros años, aumentando a 128 horas en el tercer año. "
                  "Esto permite a los estudiantes aplicar sus conocimientos en contextos reales.")

    with tab5:
        st.write("**Equivalencias con Otras Carreras o Programas**")
        st.write("Las equivalencias pueden variar según la institución. "
                  "Es recomendable consultar directamente con la institución educativa para obtener información específica "
                  "sobre posibles equivalencias con otras carreras o programas de estudio relacionados.")

    with tab6:
        st.write("**Tipos de Prácticas Profesionalizantes**")
        st.write("Las prácticas profesionalizantes se llevan a cabo en entornos reales o simulados, "
                  "donde los estudiantes abordan problemas específicos relacionados con la ciencia de datos "
                  "y la inteligencia artificial. Estas prácticas están diseñadas para vincular la teoría con la práctica "
                  "y se desarrollan en colaboración con organizaciones del sector.")

if tecnicatura == "Tecnicatura Superior en Administración Financiera":
    st.write(f"Has seleccionado {tecnicatura}. Aquí tienes información relevante sobre esta tecnicatura.")

    # Pestañas para Administración Financiera
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(
        ["Carga Horaria", "Distribución de Horas", "Materias Correlativas", "Prácticas Profesionalizantes", 
         "Horas de Prácticas", "Habilidades", "Planificación", "Objetivos", "Salidas Laborales", 
         "Requisitos de Ingreso", "Equivalencias"]
    )

    with tab1:
        st.write("**Carga Horaria Total**")
        st.write("La carga horaria total es de 1824 horas reloj, distribuidas a lo largo de 32 semanas anuales durante un período de 3 años.")

    with tab2:
        st.write("**Distribución de Horas entre Campos Formativos**")
        st.write("""
        - Formación General: 192 horas (11%)
        - Formación de Fundamento: 416 horas (23%)
        - Formación Específica: 736 horas (40%)
        - Prácticas Profesionalizantes: 480 horas (26%)
        """)

    with tab3:
        st.write("**Materias Correlativas para el Segundo Año**")
        st.write("""
        Algunas materias correlativas incluyen:
        - Contabilidad de Gestión (debe tener aprobado Principios de Contabilidad)
        - Matemática Financiera (debe tener aprobado Fundamentos de Matemática)
        - Práctica Profesionalizante 2 (debe tener aprobado Práctica Profesionalizante 1)
        """)

    with tab4:
        st.write("**Prácticas Profesionalizantes**")
        st.write("Las prácticas profesionalizantes son experiencias que permiten a los estudiantes aplicar los conocimientos adquiridos en un entorno laboral real. Deben ser organizadas, implementadas y evaluadas por la institución educativa, bajo el control de la respectiva Jurisdicción. Estas prácticas integran saberes de otros campos del plan de estudios y fomentan habilidades transversales.")

    with tab5:
        st.write("**Horas de Prácticas Profesionalizantes por Año**")
        st.write("""
        - Primer año: 96 horas
        - Segundo año: 128 horas
        - Tercer año: 256 horas
        """)

    with tab6:
        st.write("**Habilidades Desarrolladas**")
        st.write("Las prácticas profesionalizantes permiten desarrollar habilidades como el trabajo en equipo, la resolución de problemas y promueven una visión global e integrada de la formación, eliminando la fragmentación entre teoría y práctica.")

    with tab7:
        st.write("**Enfoque en la Planificación de Prácticas Profesionalizantes**")
        st.write("En la planificación de las prácticas profesionalizantes se debe incluir un enfoque de género que garantice la equidad en el acceso a estas instancias de aprendizaje, asegurando que todos los estudiantes tengan las mismas oportunidades.")

    with tab8:
        st.write("**Objetivos Específicos de la Carrera**")
        st.write("""
        - Formar profesionales capaces de comprender y gestionar la complejidad de las organizaciones sociales en el contexto actual.
        - Proporcionar herramientas y conocimientos que permitan a los graduados intervenir de manera crítica y propositiva en las organizaciones.
        - Desarrollar competencias técnicas en administración, finanzas y contabilidad, que faciliten la toma de decisiones informadas en el ámbito financiero.
        - Promover la creación de proyectos innovadores que contribuyan al desarrollo de emprendimientos y al empleo en un marco de economía justa y solidaria.
        """)

    with tab9:
        st.write("**Salidas Laborales**")
        st.write("""
        La Tecnicatura Superior en Administración Financiera ofrece diversas salidas laborales, tales como:
        - Administrador financiero en empresas y organizaciones.
        - Asesor en gestión financiera y contable.
        - Analista de costos y presupuestos.
        - Gestor de proyectos de inversión.
        - Consultor en negocios internacionales y mercados financieros.
        - Profesional en entidades bancarias y financieras, así como en organismos públicos y privados relacionados con la administración y finanzas.
        """)

    with tab10:
        st.write("**Requisitos de Ingreso**")
        st.write("""
        Los requisitos de ingreso para la Tecnicatura Superior en Administración Financiera incluyen:
        - Título de educación secundaria completo o su equivalente.
        - En algunos casos, se puede requerir la aprobación de un examen de ingreso o entrevista personal, dependiendo de la institución que ofrezca la carrera.
        - Se recomienda tener conocimientos básicos en matemáticas y contabilidad, aunque no siempre es un requisito formal.
        """)

    with tab11:
        st.write("**Equivalencias con Otras Carreras**")
        st.write("""
        Sí, la Tecnicatura Superior en Administración Financiera contempla equivalencias con otras carreras, especialmente aquellas que tienen trayectorias afines en el ámbito de la educación secundaria técnica. 
        Las equivalencias son:
        - Los ingresantes que acrediten trayectorias afines de Educación Secundaria Técnica, aprobadas por la Dirección General de Cultura y Educación (DGCyE), pueden presentar la certificación correspondiente para acreditar unidades curriculares según los criterios establecidos en el diseño curricular de la carrera.
        - Además, se prevé la articulación con otras titulaciones de Educación Secundaria Técnica, lo que permite a los estudiantes avanzar en su formación y facilitar su inserción en el campo laboral.
        """)

    







# Sección de Instituto
elif opcion == "Instituto":
    st.subheader("Información sobre el Instituto")
    info = st.selectbox("Elige la información que buscas:", 
                        ["Documentación",  "Inscripción", 
                         "Requisitos de Ingreso", "Instagram/Facebook"],
                        key='info_opcion')
    
    if info == "Documentación":
     st.write("""
     - Realizar Preinscripción (SIN EXCEPCIÓN): Aquí.
      - Fotocopia del Certificado analítico de estudios, con Número de Registro en la Provincia de Buenos Aires o Certificado de Título en trámite, no sirve el de alumno regular (SIN EXCEPCIÓN).
     - Fotocopia del D.N.I. (SIN EXCEPCIÓN).
     - Certificado de aptitud psico-física, firmado por un profesional médico. (No sirve «goza de buena salud»).
     - Una foto tipo carnet.
     - Planilla de Inscripción completa e impresa en hoja oficio: [Planilla de inscripción a carrera](#).
     - Presentar toda la documentación solicitada a partir del 1/12.
     - La documentación se entrega en folio tamaño oficio, sin excepción.
     """)

    elif info == "Inscripción":
        st.write("Inscripción abierta desde marzo a julio. Para más detalles, consulta la página web.")
        st.markdown ("[Información para Ingresantes](http://www.i12.com.ar/i12/?page_id=2056).")

    elif info == "Requisitos de Ingreso":
        st.write("""
        **REQUISITOS DE INGRESO:**

        - Haber completado los estudios de Nivel Medio/Secundario o tener certificado de título en trámite, no se acepta el de alumno regular.
        - Pre-inscribirse.
        - Presentar la documentación.
        - Acreditar el Curso Inicial.
        

        **Información adicional:**
        - Los inscriptos en la carrera TS en Ceremonial y Protocolo, comisión 1°2°, deben escribir al email documentacionceremoniali12@gmail.com, asunto «Ingresante» por la entrega de documentación.
        - Los inscriptos en la carrera TS en Higiene y Seguridad en el Trabajo que se encuentren en lista de espera serán reubicados en otras comisiones hasta que se genere la vacante en el turno solicitado. 
        - Entregar la documentación.

        **Horario de recepción de documentación:**
        - Turno Mañana: de 9:00 a 12:00 HS.
        - Turno Tarde: de 14:00 a 17:00 HS.
        - Turno Noche: de 19:00 a 22:00 HS.

        En la página del instituto se informará sobre los días y horarios en los que deberá concurrir a realizar el Curso Inicial obligatorio que deben realizar los aspirantes a las carreras. El curso de ingreso inicia en marzo; se confirmará la fecha de inicio por la página web.
        """)
    elif info == "Instagram/Facebook":
        col1,col2,col3,col4,col5 = st.columns(5) 
        st.write("Síguenos en nuestras redes sociales para estar al tanto de las novedades.")
        
        col1.image ("instagram.png", width = 50)
        col1.markdown ("[Instagram](https://www.instagram.com/instituto12laplata?igsh=cTNjNHpicmJiazYw).")
        




# Sección de Encuesta personal
elif opcion == "Encuesta personal":
    st.subheader("Encuesta personal")

    # Formulario de encuesta
    with st.form("Formulario de Encuesta"):
        # Datos personales
        st.header("Datos Personales")
        nombre = st.text_input("Nombre", key='nombre_input')
        apellido = st.text_input("Apellido", key='apellido_input')
        fecha_nacimiento = st.date_input("Fecha de Nacimiento", key='fecha_nacimiento_input')
        dni = st.text_input("DNI", key='dni_input')
        cuil = st.text_input("CUIL", key='cuil_input')
        nacionalidad = st.text_input("Nacionalidad", key='nacionalidad_input')
        tiene_hijos = st.radio("¿Tiene hijos?", ("Sí", "No"), key='tiene_hijos_radio')
        
        # Domicilio
        st.header("Domicilio")
        calle = st.text_input("Calle", key='calle_input')
        numero = st.text_input("Nº", key='numero_input')
        codigo_postal = st.text_input("Código Postal", key='codigo_postal_input')
        provincia = st.text_input("Provincia", key='provincia_input')
        localidad = st.text_input("Localidad", key='localidad_input')
        telefono = st.text_input("Número de Teléfono", key='telefono_input')
        correo = st.text_input("Correo Electrónico", key='correo_input')

        # Información de salud
        st.header("Información de Salud")
        padece_condicion = st.radio("¿Padece o ha padecido alguna condición de salud?", ("Sí", "No"), key='padece_condicion_radio')
        condicion_cual = st.text_input("¿Cuál?", key='condicion_cual_input') if padece_condicion == "Sí" else ""
        alergia_grave = st.radio("¿Padece o ha padecido algún tipo de alergia grave?", ("Sí", "No"), key='alergia_grave_radio')
        alergia_cual = st.text_input("¿Cuál?", key='alergia_cual_input') if alergia_grave == "Sí" else ""
        medicacion = st.radio("¿Recibe de manera habitual algún tipo de medicación?", ("Sí", "No"), key='medicacion_radio')
        operacion = st.radio("¿Tuvo alguna operación?", ("Sí", "No"), key='operacion_radio')
        motivo_operacion = st.text_input("En caso afirmativo, ¿por qué motivo?", key='motivo_operacion_input') if operacion == "Sí" else ""
        obra_social = st.radio("¿Posee obra social?", ("Sí", "No"), key='obra_social_radio')
        obra_social_nombre = st.text_input("Obra Social", key='obra_social_nombre_input') if obra_social == "Sí" else ""
        numero_afiliado = st.text_input("Nº Afiliado", key='numero_afiliado_input') if obra_social == "Sí" else ""

        # Estudios cursados
        st.header("Estudios Cursados")
        secundaria_completo = st.radio("¿Tiene secundaria completa?", ("Sí", "No"), key='secundaria_completo_radio')
        instituto_titulo = st.text_input("Instituto que emite el título", key='instituto_titulo_input') if secundaria_completo == "Sí" else ""
        otros_estudios = st.text_area("Otros estudios superiores realizados", key='otros_estudios_text_area')

        # Botón para enviar el formulario
        enviado = st.form_submit_button("Enviar")

        if enviado:
            # Configurar el servidor SMTP
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_user = 'tu_email@gmail.com'  # Cambia a tu correo electrónico
            smtp_password = 'tu_contraseña'  # Cambia a tu contraseña

            # Crear el mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = smtp_user
            mensaje['To'] = 'bibliotecaidoce@gmail.com'
            mensaje['Subject'] = Header('Formulario de Encuesta Personal', 'utf-8')

            cuerpo = f"""
            Datos Personales:
            Nombre: {nombre}
            Apellido: {apellido}
            Fecha de Nacimiento: {fecha_nacimiento}
            DNI: {dni}
            CUIL: {cuil}
            Nacionalidad: {nacionalidad}
            ¿Tiene hijos?: {tiene_hijos}

            Domicilio:
            Calle: {calle}
            Nº: {numero}
            Código Postal: {codigo_postal}
            Provincia: {provincia}
            Localidad: {localidad}
            Número de Teléfono: {telefono}
            Correo Electrónico: {correo}

            Información de Salud:
            ¿Padece o ha padecido alguna condición de salud?: {padece_condicion}
            ¿Cuál?: {condicion_cual}
            ¿Padece o ha padecido algún tipo de alergia grave?: {alergia_grave}
            ¿Cuál?: {alergia_cual}
            ¿Recibe de manera habitual algún tipo de medicación?: {medicacion}
            ¿Tuvo alguna operación?: {operacion}
            En caso afirmativo, ¿por qué motivo?: {motivo_operacion}
            ¿Posee obra social?: {obra_social}
            Obra Social: {obra_social_nombre}
            Nº Afiliado: {numero_afiliado}

            Estudios Cursados:
            ¿Tiene secundaria completa?: {secundaria_completo}
            Instituto que emite el título: {instituto_titulo}
            Otros estudios superiores realizados: {otros_estudios}
            """
            # Usar UTF-8 para el cuerpo del mensaje
            mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

            # Enviar el mensaje
            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_password)
                    server.send_message(mensaje)
                st.success("Formulario enviado correctamente.")
            except Exception as e:
                st.error(f"No se pudo enviar el formulario. Error: {e}")


# Sección de Test vocacional
elif opcion == "Test vocacional":
    st.subheader("Test vocacional")

    # Definición de preguntas y opciones
    preguntas = {
        "¿Cómo te sientes trabajando con tecnología y sistemas?": [
            "Me encanta descubrir cómo los dispositivos se conectan e interactúan entre sí.",
            "Me interesa analizar y resolver problemas complejos de sistemas informáticos.",
            "Disfruto desarrollando software y creando nuevas aplicaciones.",
            "No tengo mucho interés en la tecnología, prefiero enfocarme en aspectos financieros o administrativos.",
            "Me interesa asegurarme de que los procesos en el trabajo sean seguros y eficientes.",
            "Prefiero trabajar en un entorno donde se gestionen eventos y ceremonias.",
            "Estoy más interesado en temas de contabilidad y finanzas.",
            "Me gustaría trabajar en la protección y seguridad de los empleados en ambientes de salud."
        ],
        "¿Qué tipo de tareas disfrutas más?": [
            "Diseñar y gestionar redes y sistemas integrados.",
            "Analizar datos y mejorar la eficiencia de los sistemas.",
            "Programar y desarrollar aplicaciones o software.",
            "Llevar a cabo tareas relacionadas con la contabilidad y la gestión de recursos financieros.",
            "Asegurar un entorno de trabajo seguro y saludable.",
            "Organizar y coordinar eventos y protocolos.",
            "Administrar y controlar aspectos financieros en una organización.",
            "Trabajar en la prevención y seguridad en entornos de salud."
        ],
        "¿Cuál de estas actividades te atrae más?": [
            "Trabajar con sistemas de Internet de las Cosas y dispositivos inteligentes.",
            "Resolver problemas técnicos y mejorar el rendimiento de los sistemas.",
            "Desarrollar programas y aplicaciones de software.",
            "Gestionar la contabilidad y los libros financieros de una empresa.",
            "Implementar y supervisar medidas de seguridad en el lugar de trabajo.",
            "Coordinar eventos y asegurarse de que se cumplan los protocolos adecuados.",
            "Planificar y controlar el flujo financiero y los presupuestos.",
            "Asegurar el cumplimiento de las normativas de salud y seguridad en el entorno laboral."
        ],
        "¿Qué habilidades te gustaría desarrollar más?": [
            "Programación y diseño de sistemas integrados.",
            "Análisis de sistemas y resolución de problemas técnicos.",
            "Desarrollo y mantenimiento de aplicaciones de software.",
            "Contabilidad y administración financiera.",
            "Implementación de medidas de seguridad y protocolos de prevención.",
            "Organización y planificación de eventos y ceremonias.",
            "Control y planificación financiera.",
            "Gestión de seguridad y salud en el entorno laboral."
        ],
        "¿Cómo te imaginas tu entorno de trabajo ideal?": [
            "En un entorno dinámico, trabajando con tecnología avanzada y sistemas inteligentes.",
            "En un lugar donde pueda analizar y mejorar la tecnología y los sistemas existentes.",
            "En una oficina de desarrollo, creando y programando nuevas aplicaciones.",
            "En una oficina de contabilidad, gestionando y analizando información financiera.",
            "En un entorno enfocado en la seguridad, implementando y supervisando normas de prevención.",
            "En un entorno relacionado con la organización de eventos y protocolo.",
            "En una oficina financiera, manejando presupuestos y planes financieros.",
            "En un entorno de salud, asegurando la protección y bienestar de los trabajadores."
        ],
        "¿Cuál es tu principal motivación para elegir una carrera?": [
            "Trabajar con tecnología avanzada y sistemas innovadores.",
            "Resolver problemas complejos y mejorar sistemas tecnológicos.",
            "Crear y desarrollar nuevas aplicaciones y software.",
            "Gestionar finanzas y contabilidad de manera efectiva.",
            "Asegurar un entorno laboral seguro y saludable.",
            "Coordinar eventos y garantizar el cumplimiento de protocolos.",
            "Planificar y controlar aspectos financieros en una empresa.",
            "Garantizar la seguridad y salud en el entorno laboral."
        ]
    }

    respuestas = {pregunta: st.selectbox(pregunta, opciones, key=f'respuesta_{pregunta}') for pregunta, opciones in preguntas.items()}
    
    if st.button("Finalizar Test"):
        # Definir descripciones para cada carrera
        descripciones = {
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos": "Se centra en el diseño y gestión de redes y sistemas integrados que utilizan Internet de las Cosas (IoT) y dispositivos embebidos.",
            "Tecnicatura Superior en Análisis de Sistemas": "Se enfoca en el análisis, diseño y mejora de sistemas informáticos, con un enfoque en la resolución de problemas técnicos.",
            "Tecnicatura Superior en Desarrollo de Software": "Está orientada a la creación, desarrollo y mantenimiento de aplicaciones y software para diversas plataformas.",
            "Tecnicatura Superior en Administración Contable": "Aborda la gestión contable y administrativa de una empresa, incluyendo la preparación de informes financieros y auditoría.",
            "Tecnicatura Superior en Administración Financiera": "Se dedica a la planificación, gestión y control de recursos financieros dentro de una organización.",
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo": "Se especializa en implementar y supervisar políticas y medidas de seguridad para garantizar un entorno de trabajo seguro y saludable.",
            "Tecnicatura Superior en Ceremonial y Protocolo": "Enfocada en la organización y coordinación de eventos, ceremonias y protocolos, garantizando su correcta ejecución.",
            "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud": "Se centra en la protección y seguridad de los empleados en el entorno de salud, asegurando el cumplimiento de normativas y protocolos."
        }

        # Definir la lógica para asignar puntos a cada carrera
        puntuaciones = {
            "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos": 0,
            "Tecnicatura Superior en Análisis de Sistemas": 0,
            "Tecnicatura Superior en Desarrollo de Software": 0,
            "Tecnicatura Superior en Administración Contable": 0,
            "Tecnicatura Superior en Administración Financiera": 0,
            "Tecnicatura Superior en Higiene y Seguridad en el Trabajo": 0,
            "Tecnicatura Superior en Ceremonial y Protocolo": 0,
            "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud": 0
        }

        # Mapear respuestas a carreras
        respuestas_carrera = {
            "Me encanta descubrir cómo los dispositivos se conectan e interactúan entre sí.": "Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos",
            "Me interesa analizar y resolver problemas complejos de sistemas informáticos.": "Tecnicatura Superior en Análisis de Sistemas",
            "Disfruto desarrollando software y creando nuevas aplicaciones.": "Tecnicatura Superior en Desarrollo de Software",
            "No tengo mucho interés en la tecnología, prefiero enfocarme en aspectos financieros o administrativos.": ["Tecnicatura Superior en Administración Contable", "Tecnicatura Superior en Administración Financiera"],
            "Me interesa asegurarme de que los procesos en el trabajo sean seguros y eficientes.": ["Tecnicatura Superior en Higiene y Seguridad en el Trabajo", "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud"],
            "Prefiero trabajar en un entorno donde se gestionen eventos y ceremonias.": "Tecnicatura Superior en Ceremonial y Protocolo",
            "Estoy más interesado en temas de contabilidad y finanzas.": ["Tecnicatura Superior en Administración Contable", "Tecnicatura Superior en Administración Financiera"],
            "Me gustaría trabajar en la protección y seguridad de los empleados en ambientes de salud.": "Certificación Superior en Salud y Seguridad Ocupacional en el Trabajo en los Establecimientos de Salud"
        }

        # Asignar puntos a cada carrera según las respuestas
        for pregunta, respuesta in respuestas.items():
            if respuesta in respuestas_carrera:
                carreras = respuestas_carrera[respuesta]
                if isinstance(carreras, list):
                    for carrera in carreras:
                        puntuaciones[carrera] += 1
                else:
                    puntuaciones[carreras] += 1
        
        # Ordenar carreras por puntuación
        carreras_ordenadas = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
        
        # Mostrar las 3 principales recomendaciones
        st.write("Basado en tus respuestas, aquí tienes las 3 carreras que podrían ser más adecuadas para ti:")

        for carrera, _ in carreras_ordenadas[:3]:
            st.write(f"**{carrera}:** {descripciones[carrera]}")


import streamlit as st
import streamlit.components.v1 as components

import streamlit as st
import streamlit.components.v1 as components

# Verifica si la opción seleccionada es "Ingreso"
if opcion == "Ingreso":
    st.subheader("Ingreso")
    st.title("Asistente Virtual - Nova")

    # HTML y CSS para simular un chat estilo WhatsApp
    html_code = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .chat-container {
                width: 100%;
                max-width: 600px;
                margin: auto;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                background-color: #f8f9fa;
            }
            .chat-box {
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                height: 400px;
                overflow-y: auto;
                background-color: #e5ddd5;
            }
            .message {
                display: inline-block;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 10px;
                max-width: 70%;
                font-size: 14px;
            }
            .user-message {
                background-color: #dcf8c6;
                align-self: flex-end;
                margin-left: auto;
            }
            .bot-message {
                background-color: #fff;
                align-self: flex-start;
                margin-right: auto;
            }
            #chat-log {
                display: flex;
                flex-direction: column;
            }
            .chat-input {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <div class="chat-box">
                <div id="chat-log"></div>
            </div>
            <form id="chat-form" class="chat-input">
                <input type="text" id="user-message" placeholder="Escribe tu mensaje aquí..." class="form-control">
                <button type="submit" class="btn btn-primary mt-2">Enviar</button>
            </form>
        </div>

        <script>
            var firstMessage = true;

            document.getElementById('chat-form').onsubmit = function (e) {
                e.preventDefault();
                var message = document.getElementById('user-message').value;

                // Mostrar el mensaje del usuario
                var chatLog = document.getElementById('chat-log');
                var userMessageDiv = document.createElement("div");
                userMessageDiv.className = "message user-message";
                userMessageDiv.innerHTML = `<strong>Tú:</strong> ${message}`;
                chatLog.appendChild(userMessageDiv);

                // Respuesta de Nova
                var response;
                if (firstMessage && isGreeting(message)) {
                    response = "¡Buen día! Soy Nova, tu asistente virtual. Ten en cuenta que estoy limitado a responder solo ciertas consultas, pero haré lo mejor que pueda para ayudarte. ¡Gracias por tu paciencia!";
                    firstMessage = false;
                } else if (firstMessage) {
                    response = "¡Hola! Para comenzar, por favor salúdame. Ten en cuenta que estoy en versión beta, por lo que puedo tener algunos errores. ¡Gracias por tu comprensión!.";
                } else {
                    response = getResponse(message);
                }

                // Mostrar la respuesta de Nova
                var botMessageDiv = document.createElement("div");
                botMessageDiv.className = "message bot-message";
                botMessageDiv.innerHTML = `<strong>Nova:</strong> ${response}`;
                chatLog.appendChild(botMessageDiv);

                // Limpiar input
                document.getElementById('user-message').value = '';  

                // Scroll automático al final del chat
                chatLog.scrollTop = chatLog.scrollHeight;
            };

            function isGreeting(message) {
                const greetings = ["hola", "buen día", "buenas tardes", "buenas noches", "hey", "saludos","Hola","holi","buenas"];
                var lowerMessage = message.toLowerCase();
                return greetings.some(greeting => lowerMessage.includes(greeting));
            }

            function getResponse(message) {
                const responses = [
                    { pattern: /requisitos.*ingresar/i, response: "Los requisitos para ingresar son: Haber completado los estudios secundarios o tener el certificado de título en trámite. Preinscribirse. Haber completado la planilla para inscripción en la carrera deseada y Acreditar el curso inicial." },
                    { pattern: /requisitos.*inscribirme/i, response: "Los requisitos para inscribirse son: Haber realizado la preinscripción, fotocopia del certificado analítico de estudios con número de registro en la provincia de Buenos Aires o certificado de título en trámite, fotocopia del DNI, certificado de aptitud psico-física, una foto tipo carnet, y presentar toda la documentación en un folio tamaño oficio." },
                    { pattern: /fecha.*límite/i, response: "La fecha límite para inscribirse es el 8 de marzo." },
                    { pattern: /inscripción.*en línea/i, response: "La inscripción se hace de manera presencial, en el Instituto." },
                    { pattern: /donde.*presentar.*documentación/i, response: "La documentación se debe presentar en la biblioteca del Instituto." },
                    { pattern: /me.*inscribir.*sin.*título/i, response: "Sí, te puedes inscribir presentando un certificado de título en trámite." },
                    { pattern: /carreras/i, response: "Las carreras que puedes cursar son: Tecnicatura Superior en Análisis de Sistemas, Técnicatura Superior en Desarrollo de Software, Técnicatura Superior en Ceremonial y Protocolo, Técnicatura Superior en Higiene y Seguridad en el Trabajo, Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Tecnicatura Superior en Internet de las Cosas y Sistemas Embebidos, Técnicatura Superior en Administración Contable, Técnicatura Superior en Administración Financiera." },
                    { pattern: /materias.*primer.*año/i, response: "Las materias de primer año para la Tecnicatura Superior en Administración Contable son: Derecho, Inglés 1, Principios de Administración, Economía, Fundamentos de Matemáticas, Principios de Contabilidad, Gestión Administrativo Contable y Práctica Profesionalizantes." },
                    { pattern: /duración.*carrera/i, response: "La Tecnicatura Superior en Administración Contable es una carrera de tres años y sus materias son anuales." },
                    { pattern: /curso.*ingreso/i, response: "Se debe realizar un curso de ingreso que no es eliminatorio." },
                    { pattern: /horario/i, response: "Puedes cursar de mañana (8 a 12), de tarde (13 a 17) o de noche (18 a 22)." },
                    { pattern: /modalidad/i, response: "Las cursadas son presenciales." },
                    { pattern: /cuando.*empiezan.*clases/i, response: "Las clases comienzan en abril." },
                    { pattern: /función.*técnico.*administración.*contable/i, response: "Algunas de las funciones de un técnico superior en administración contable son: Registrar contablemente las operaciones, coordinar procesos de producción, gestionar recursos para compras y contrataciones, coordinar y supervisar al personal del área comercial, proponer y coordinar políticas de producción y organizar el área financiera de la empresa." },
                    { pattern: /trabajar.*técnico.*administración.*contable/i, response: "Podrás trabajar en cualquier organización pública o privada, ya que el egresado está preparado para resolver situaciones y llevar adelante las funciones administrativas sin importar el tamaño de la organización." },
                    { pattern: /documentos.*necesito/i, response: "Para inscribirte, necesitas: haber completado los estudios de Nivel Medio/Secundario, pre-inscribirte, presentar documentación, acreditar el Curso Inicial, fotocopia del Certificado analítico de estudios, fotocopia del D.N.I., certificado de aptitud psico-física, una foto tipo carnet y la planilla de inscripción completa." },
                    { pattern: /inscripción.*exitosa/i, response: "Para verificar si tu inscripción fue exitosa, ingresa a la autogestión de alumnos con tu DNI como usuario y contraseña." },
                    { pattern: /cursos.*disponibles/i, response: "Ofrecemos carreras como Tecnicatura Superior en Internet de las Cosas, Ciencia de Datos, Análisis de Sistemas, Desarrollo de Software, Administración Contable, Higiene y Seguridad, entre otras." },
                    { pattern: /dirección|ubicación|calle/i, response: "La dirección del Instituto es: Avda. 7 Nro. 2149 esq. 76. Para ver la ubicación, puedes seguir este enlace: <a href='https://maps.app.goo.gl/vrZbcD8JJDhkjXkR7' target='_blank'>Ver en Google Maps</a>" },
                    { pattern: /gracias|ok|buenisimo|perfecto/i, response: "¡De nada! Para más información, puedes visitar el siguiente enlace: <a href='http://www.i12.com.ar/i12/' target='_blank'>http://www.i12.com.ar/i12/</a>" }
                ];

                for (const { pattern, response } of responses) {
                    if (pattern.test(message)) {
                        return response;
                    }
                }
                return "Lo siento, no tengo información sobre eso.";
            }
        </script>
    </body>
    </html>
    """

    # Renderizar el HTML personalizado en Streamlit
    components.html(html_code, height=600)
