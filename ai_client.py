import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargar variables del archivo .env
load_dotenv()

# 2. Configurar la API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("CRÍTICO: No se encontró GOOGLE_API_KEY en el archivo .env")

genai.configure(api_key=api_key)

# 3. Configuración del modelo
generation_config = {
    "temperature": 0.7,
    "max_output_tokens": 800,
}

# CAMBIO FINAL: Usamos el alias 'gemini-flash-latest' que aparecía en tu lista.
# Este apunta siempre a la versión rápida y gratuita más estable.
model = genai.GenerativeModel(
    model_name="gemini-flash-latest", 
    generation_config=generation_config
)

def call_llm(prompt):
    """
    Función modular para llamar a la IA.
    """
    try:
        # Rate Limit: Esperamos un poco para no saturar
        time.sleep(2)
        
        # Llamada a la API
        response = model.generate_content(prompt)
        
        # Devolver texto
        return response.text

    except Exception as e:
        return f"Error del proveedor de IA: {str(e)}"