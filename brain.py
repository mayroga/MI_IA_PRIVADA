import os
import openai
import google.generativeai as genai
import requests
from dotenv import load_dotenv

load_dotenv()

# ===============================
# SISTEMA MAESTRO DE INSTRUCCIÓN
# ===============================
INSTRUCCION_MAESTRA = (
    "Actúa como el mejor Ingeniero de Software del Mundo. "
    "Entrega SOLO código funcional listo para producción. "
    "No explicaciones, no saludos, no texto innecesario."
)

# ===============================
# OPENAI
# ===============================
def motor_openai(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        client = openai.OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": INSTRUCCION_MAESTRA},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content

    except Exception:
        return None


# ===============================
# GEMINI
# ===============================
def motor_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None

    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={"temperature": 0.1}
        )

        full_prompt = f"{INSTRUCCION_MAESTRA}\n\n{prompt}"
        response = model.generate_content(full_prompt)

        return response.text

    except Exception:
        return None


# ===============================
# OLLAMA LOCAL (GRATIS)
# ===============================
def motor_local(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"{INSTRUCCION_MAESTRA}\n\n{prompt}",
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json().get("response")

        return None

    except Exception:
        return None


# ===============================
# MOTOR CENTRAL (HÍBRIDO PRO)
# ===============================
def generar_codigo_maestro(prompt, motor="auto"):
    """
    Motor híbrido inteligente:
    - auto: intenta OpenAI → Gemini → Local
    - OpenAI: fuerza OpenAI
    - Gemini: fuerza Gemini
    - Local: fuerza Ollama
    """

    try:

        # =======================
        # MODO AUTOMÁTICO (RECOMENDADO)
        # =======================
        if motor == "auto":

            # 1. OpenAI
            resultado = motor_openai(prompt)
            if resultado:
                return resultado

            # 2. Gemini
            resultado = motor_gemini(prompt)
            if resultado:
                return resultado

            # 3. Local
            resultado = motor_local(prompt)
            if resultado:
                return resultado

            return "ERROR: Ningún motor disponible."

        # =======================
        # FORZADOS
        # =======================
        elif motor == "OpenAI":
            return motor_openai(prompt) or "ERROR OpenAI"

        elif motor == "Gemini":
            return motor_gemini(prompt) or "ERROR Gemini"

        elif motor == "Local":
            return motor_local(prompt) or "ERROR Local (Ollama no activo)"

        else:
            return "ERROR: Motor no válido."

    except Exception as e:
        return f"ERROR CRÍTICO: {str(e)}"
