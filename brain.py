import os
import openai
import google.generativeai as genai
import requests
from dotenv import load_dotenv

load_dotenv()

# ===============================
# CONFIGURACIÓN
# ===============================
OLLAMA_URL = "http://localhost:11434/api/generate"
TIMEOUT = 60

# ===============================
# SISTEMA MAESTRO
# ===============================
INSTRUCCION_MAESTRA = (
    "Actúa como el mejor Ingeniero de Software del Mundo. "
    "Entrega SOLO código funcional listo para producción. "
    "No explicaciones, no saludos, no texto innecesario."
)

# ===============================
# VERIFICAR OLLAMA ACTIVO
# ===============================
def ollama_activo():
    try:
        r = requests.get("http://localhost:11434", timeout=2)
        return r.status_code == 200
    except:
        return False

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
    if not ollama_activo():
        return None

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": f"{INSTRUCCION_MAESTRA}\n\n{prompt}",
                "stream": False
            },
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("response")

        return None

    except Exception:
        return None

# ===============================
# MOTOR CENTRAL (HÍBRIDO PRO)
# ===============================
def generar_codigo_maestro(prompt, motor="auto"):
    """
    MODOS:
    - auto (RECOMENDADO): Local → OpenAI → Gemini
    - Local
    - OpenAI
    - Gemini
    """

    try:

        # =======================
        # AUTO INTELIGENTE (GRATIS PRIMERO)
        # =======================
        if motor == "auto":

            # 1. LOCAL GRATIS
            resultado = motor_local(prompt)
            if resultado:
                return resultado

            # 2. OPENAI
            resultado = motor_openai(prompt)
            if resultado:
                return resultado

            # 3. GEMINI
            resultado = motor_gemini(prompt)
            if resultado:
                return resultado

            return "ERROR: Ningún motor disponible."

        # =======================
        # FORZADOS
        # =======================
        elif motor == "Local":
            return motor_local(prompt) or "ERROR: Ollama no activo"

        elif motor == "OpenAI":
            return motor_openai(prompt) or "ERROR OpenAI"

        elif motor == "Gemini":
            return motor_gemini(prompt) or "ERROR Gemini"

        else:
            return "ERROR: Motor no válido"

    except Exception as e:
        return f"ERROR CRÍTICO: {str(e)}"
