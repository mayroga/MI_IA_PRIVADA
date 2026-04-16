import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Carga de variables de entorno (Configuradas en el Dashboard de Render)
load_dotenv()

def generar_codigo_maestro(prompt, motor):
    """
    Motor central de inteligencia de AL CIELO.
    Genera arquitectura de software de alta precisión.
    """
    
    # SYSTEM PROMPT: Configuración de Experto Absoluto
    instruccion_maestra = (
        "Actúa como el mejor Ingeniero de Software del Mundo. Tu objetivo es entregar "
        "soluciones técnicas perfectas, sin errores de sintaxis y listas para producción. "
        "REGLAS DE SALIDA:\n"
        "1. Entrega EXCLUSIVAMENTE código funcional y archivos estructurados.\n"
        "2. No saludes, no des introducciones ni conclusiones innecesarias.\n"
        "3. Si el sistema es de logística, aplica estándares de cumplimiento (IATA, DOT, CBP).\n"
        "4. No menciones 'IA' ni 'Inteligencia Artificial' bajo ningún concepto.\n"
        "5. Usa tablas en Markdown si necesitas explicar estructuras de datos."
    )

    try:
        # --- MOTOR 1: OPENAI (EXTRA) ---
        if motor == "OpenAI (Extra)":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "ERROR: Falta OPENAI_API_KEY en las variables de entorno de Render."
            
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": instruccion_maestra},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1  # Máxima precisión técnica
            )
            return response.choices[0].message.content

        # --- MOTOR 2: GEMINI (EXTRA) ---
        elif motor == "Gemini (Extra)":
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return "ERROR: Falta GEMINI_API_KEY en las variables de entorno de Render."
            
            genai.configure(api_key=api_key)
            # Usamos gemini-1.5-flash por su estabilidad y velocidad en APIs
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={"temperature": 0.1}
            )
            
            # Formato de envío optimizado
            full_prompt = f"{instruccion_maestra}\n\nINSTRUCCIÓN DEL USUARIO: {prompt}"
            response = model.generate_content(full_prompt)
            return response.text

        # --- MOTOR 3: RENDER LOCAL ---
        else:
            return (
                "### AL CIELO: INFRAESTRUCTURA LOCAL\n"
                "El motor local está activo. Para generar códigos complejos, "
                "por favor selecciona OpenAI o Gemini en el panel lateral.\n\n"
                "Estructura recomendada para tu próximo proyecto:\n"
                "| Archivo | Función | Estado |\n"
                "| :--- | :--- | :--- |\n"
                "| `app.py` | Lógica Backend | Pendiente |\n"
                "| `index.html` | Interfaz Usuario | Pendiente |\n"
                "| `schema.sql` | Base de Datos | Pendiente |"
            )

    except Exception as e:
        # Captura de errores de cuota, red o claves
        return f"ERROR CRÍTICO EN EL MOTOR: {str(e)}"
