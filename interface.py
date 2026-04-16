import streamlit as st # Herramienta ideal para interfaces de IA privadas
from brain import CodeArchitect
from factory import create_project_structure

st.title("AL CIELO - Software Factory")
st.subheader("Generador de Sistemas de Alta Precisión")

instruction = st.text_area("Describe el sistema o app que necesitas (Ej: Un sistema de logística con SQL y PDF):")
project_name = st.text_input("Nombre del proyecto:", "mi_nueva_app")

if st.button("GENERAR CÓDIGO MAESTRO"):
    architect = CodeArchitect(api_key="TU_LLAVE_AQUÍ")
    with st.spinner("La IA está diseñando la arquitectura..."):
        raw_code = architect.generate_system(instruction)
        
        # Lógica para separar el código en archivos (puedes pedirle JSON a la IA)
        st.code(raw_code, language='python')
        st.success("Código generado. Listo para despliegue.")
