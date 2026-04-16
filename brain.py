import openai # O la librería de Google Generative AI
import os

class CodeArchitect:
    def __init__(self, api_key):
        self.api_key = api_key
        # Configuración para que actúe como el mejor programador del mundo
        self.system_prompt = (
            "Eres el mejor Ingeniero de Software del mundo. Tu salida debe ser "
            "EXCLUSIVAMENTE código funcional, sin explicaciones, sin errores y "
            "con comentarios técnicos breves. Estructura siempre los archivos listos "
            "para copiar y pegar."
        )

    def generate_system(self, instruction):
        # Aquí conectas con el modelo (GPT-4o o Gemini 1.5 Pro)
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4o", # O el modelo de tu preferencia
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": instruction}
            ],
            temperature=0.1 # Baja temperatura para evitar errores y alucinaciones
        )
        return response.choices[0].message.content

# El motor está listo para recibir cualquier orden de creación
