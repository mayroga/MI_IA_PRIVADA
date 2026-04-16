import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generar_codigo_maestro(prompt, motor):
    """
    Asesoría técnica de alta precisión. 
    Prioridad: Lógica Python Local de AL CIELO.
    """
    
    # SYSTEM PROMPT: Configuración de Especialista en Carga y Software
    instruccion_maestra = (
        "Eres el mejor Ingeniero de Software. Especialista en normativas IATA, DOT y CBP. "
        "Entrega soluciones técnicas directas y archivos listos para producción. "
        "REGLAS: No digas IA. No des explicaciones largas. Usa tablas para datos."
    )

    try:
        if motor == "Motor Render Local":
            return generar_logica_python_local(prompt)

        elif motor == "OpenAI (Extra)":
            api_key = os.getenv("OPENAI_API_KEY")
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": instruccion_maestra},
                          {"role": "user", "content": prompt}],
                temperature=0.1
            )
            return response.choices[0].message.content

        elif motor == "Gemini (Extra)":
            api_key = os.getenv("GEMINI_API_KEY")
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"{instruccion_maestra}\n\n{prompt}")
            return response.text

    except Exception as e:
        return f"AL CIELO - Aviso: Error en API externa. Use el Motor Local. Detalle: {str(e)}"

def generar_logica_python_local(prompt):
    """
    Generador de archivos basado en lógica pura de Python (Motor Render).
    """
    p = prompt.lower()
    
    # Bloque de código base para evitar errores de f-string
    base_code = """import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "online", "msg": "Sistema AL CIELO Activo"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)"""

    # Lógica de respuesta profesional
    if "sql" in p or "base de datos" in p:
        res = "### ARQUITECTURA ESTRUCTURADA (PYTHON LOCAL)\n\n"
        res += "**Archivo: app.py**\n```python\n" + base_code + "\n```\n\n"
        res += "**Archivo: schema.sql**\n```sql\nCREATE TABLE estados (id SERIAL PRIMARY KEY, nombre VARCHAR(50));\n```"
        return res
    
    elif "avianca" in p or "carga" in p or "iata" in p:
        res = "### ASESORÍA DE CARGA PROFESIONAL (AL CIELO)\n\n"
        res += "**Archivo: logistica.py**\n
