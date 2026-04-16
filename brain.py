import os
import sys
import subprocess

def iniciar_sistema():
    """
    Configuración de arranque para AL CIELO en la infraestructura de Render.
    Asegura que el entorno sea estable antes de lanzar la interfaz.
    """
    # Definición del puerto para Render
    port = os.environ.get("PORT", "8501")
    
    print(f"--- AL CIELO: Iniciando Motor en puerto {port} ---")
    
    try:
        # Comando para ejecutar Streamlit con la configuración de red necesaria
        comando = [
            "streamlit", 
            "run", 
            "interface.py", 
            "--server.port", port, 
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ]
        
        # Ejecución del proceso
        subprocess.run(comando, check=True)
        
    except KeyboardInterrupt:
        print("\n--- Sistema AL CIELO detenido por el usuario ---")
    except Exception as e:
        print(f"ERROR CRÍTICO AL INICIAR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    iniciar_sistema()
