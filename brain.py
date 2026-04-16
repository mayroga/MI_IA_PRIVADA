from flask import Flask, request, jsonify
from brain import generar_codigo_maestro

app = Flask(__name__)

# ===============================
# FORZAR OLLAMA ACTIVO (LOCAL)
# ===============================
def ollama_activo():
    try:
        return True
    except:
        return False

# ===============================
# RUTA PRINCIPAL
# ===============================
@app.route("/")
def home():
    return "AL CIELO ENGINE ACTIVO"

# ===============================
# API GENERADOR DE CÓDIGO
# ===============================
@app.route("/generar", methods=["POST"])
def generar():

    try:
        data = request.get_json()

        prompt = data.get("prompt", "")
        motor = data.get("motor", "auto")  # auto por defecto

        if not prompt:
            return jsonify({"error": "Prompt vacío"}), 400

        resultado = generar_codigo_maestro(prompt, motor)

        return jsonify({
            "status": "ok",
            "motor": motor,
            "resultado": resultado
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "mensaje": str(e)
        }), 500


# ===============================
# TEST DIRECTO (IMPORTANTE)
# ===============================
@app.route("/test-local")
def test_local():
    try:
        resultado = generar_codigo_maestro(
            "write a simple python hello world",
            "Local"
        )

        return jsonify({
            "status": "ok",
            "resultado": resultado
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
