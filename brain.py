import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Carga de variables de entorno (Keys de Render)
load_dotenv()

def generar_codigo_maestro(prompt, motor):
    """
    Motor central de inteligencia de AL CIELO.
    Genera código de alta precisión basado en el proveedor seleccionado.
    """
    
    # SYSTEM PROMPT: Define el comportamiento de experto absoluto
    instruccion_maestra = (
        "Eres el mejor Ingeniero de Software del Mundo. Tu especialidad es crear apps y sistemas "
        "completos, sin errores, listos para copiar y pegar. "
        "REGLAS ESTRICTAS:\n"
        "1. No saludes ni des explicaciones largas.\n"
        "2. Si el usuario pide una app, entrega la estructura de archivos completa.\n"
        "3. Usa comentarios técnicos solo donde sea necesario.\n"
        "4. Si detectas lógica de logística o carga, aplica normativas IATA, DOT y CBP.\n"
        "5. No uses la palabra 'IA' ni 'Inteligencia Artificial' en tus respuestas."
    )

    try:
        # --- OPCIÓN 1: OPENAI (Extra) ---
        if motor == "OpenAI (Extra)":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "ERROR: No se encontró la OPENAI_API_KEY en las variables de entorno de Render."
            
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": instruccion_maestra},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2 # Precisión técnica alta
            )
            return response.choices[0].message.content

        # --- OPCIÓN 2: GEMINI (Extra) ---
        elif motor == "Gemini (Extra)":
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return "ERROR: No se encontró la GEMINI_API_KEY en las variables de entorno de Render."
            
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                system_instruction=instruccion_maestra
            )
            response = model.generate_content(prompt)
            return response.text

        # --- OPCIÓN 3: MOTOR RENDER LOCAL ---
        else:
            # Lógica pre-configurada para respuestas instantáneas de arquitectura
            return (
                "### SISTEMA DE ARQUITECTURA LOCAL (AL CIELO)\n"
                "Para generar código avanzado, selecciona el motor OpenAI o Gemini en la barra lateral.\n\n"
                "Estructura Base Recomendada:\n"
                "1. /backend: app.py (Flask/FastAPI)\n"
                "2. /frontend: index.html + script.js\n"
                "3. /database: schema.sql\n"
                "4. /deploy: render.yaml"
            )

    except Exception as e:
        return f"ERROR CRÍTICO EN EL MOTOR: {str(e)}"

# --- FUNCIONES DE SOPORTE TÉCNICO ---
def formatear_para_tabla(texto):
    """
    Convierte respuestas en formato de tabla para la interfaz.
    """
    # Esta función puede ser expandida para parsear JSON a tablas de Streamlit
    pass
