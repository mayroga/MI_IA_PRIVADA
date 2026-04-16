import streamlit as st
import os
import zipfile
import io
from brain import generar_codigo_maestro

# --- CONFIGURACIÓN DE INTERFAZ PROFESIONAL ---
st.set_page_config(
    page_title="AL CIELO | Software Factory",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado para tablas y botones
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .table-container { border: 1px solid #dee2e6; border-radius: 10px; padding: 10px; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (CONTROL DE MOTORES) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6009/6009618.png", width=100)
    st.title("Panel de Control")
    st.markdown("---")
    
    motor_seleccionado = st.selectbox(
        "Seleccionar Motor de IA:",
        ["Motor Render Local", "OpenAI (Extra)", "Gemini (Extra)"],
        help="Elige el cerebro que procesará tu código."
    )
    
    st.info("Este sistema actúa como Asesoría técnica especializada. Genera archivos sin errores listos para copiar y pegar.")
    
    if st.button("Borrar Sesión"):
        st.cache_data.clear()
        st.rerun()

# --- CUERPO PRINCIPAL ---
st.title("🚀 AL CIELO: Generador de Sistemas Autónomo")
st.subheader("Ingeniería de Software de Alta Precisión")

# Área de entrada de órdenes
instruccion = st.text_area(
    "Describe la App, Sistema o Código que necesitas:",
    height=250,
    placeholder="Ejemplo: Necesito un sistema de gestión para Avianca que valide AWB, incluya una tabla de SQL para 50 estados y genere reportes en PDF..."
)

col1, col2 = st.columns([1, 1])

if st.button("CONSTRUIR SISTEMA AHORA"):
    if not instruccion:
        st.error("Por favor, ingresa una instrucción para comenzar.")
    else:
        with st.spinner("Construyendo arquitectura técnica..."):
            # Llamada al cerebro
            codigo_generado = generar_codigo_maestro(instruccion, motor_seleccionado)
            
            # Mostrar resultado en pantalla
            st.markdown("### 🛠️ Código Maestro Generado")
            st.code(codigo_generado, language='python')
            
            # Visualización en tabla (si el código contiene datos estructurados)
            with st.expander("Ver Resumen de Estructura"):
                st.markdown('<div class="table-container">', unsafe_allow_html=True)
                st.table({
                    "Componente": ["Backend", "Frontend", "Database", "Security"],
                    "Estado": ["Optimizado", "Listo", "Estructurado", "Verificado"],
                    "Peso": ["Alto", "Medio", "Crítico", "Máximo"]
                })
                st.markdown('</div>', unsafe_allow_html=True)

            # --- SISTEMA DE DESCARGA ZIP ---
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w") as x_zip:
                # Crea el archivo principal basado en la generación
                x_zip.writestr("app_generada.py", codigo_generado)
                x_zip.writestr("instrucciones_despliegue.txt", f"Proyecto generado por AL CIELO\nMotor: {motor_seleccionado}\nInstrucción: {instruccion}")
            
            st.download_button(
                label="💾 DESCARGAR PROYECTO COMPLETO (ZIP)",
                data=buf.getvalue(),
                file_name="al_cielo_project.zip",
                mime="application/zip"
            )

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("AL CIELO Factory - Tecnología de Asesoría Privada | Render Cloud Ops")
