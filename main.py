import sys
import json
import datetime
import ai_client  # Importamos nuestro módulo de conexión

def log_interaction(option, prompt, response_text):
    """
    Guarda la interacción en un archivo logs.jsonl (formato JSON Lines).
    Requisito obligatorio para evidencia de ejecución.
    """
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "menu_option": option,
        "provider_model": "google/gemini-1.5-flash",
        "parameters": {"temperature": 0.7, "max_output_tokens": 800},
        "prompt_preview": prompt[:50] + "...",  # Guardamos solo el inicio para no ensuciar
        "response_length": len(response_text)
    }
    
    # Escribir en el archivo (append mode 'a')
    with open("logs.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

def main():
    print("--- ASIR IA TOOLS: Miniaplicación Python con IA Generativa ---")
    
    while True:
        print("\nSELECCIONE UNA TAREA:")
        print("1. Checklist técnico (Salida estructurada)")
        print("2. Transformación a plantilla ITIL")
        print("3. Respuesta guiada (Diagnóstico paso a paso)")
        print("4. Salir")
        
        choice = input("\nOpción (1-4): ")

        if choice == "4":
            print("Saliendo...")
            break

        if choice not in ["1", "2", "3"]:
            print("Opción no válida.")
            continue

        # --- OPCIÓN 1: CHECKLIST TÉCNICO ---
        if choice == "1":
            tema = input("Introduce el tema técnico (ej. hardening SSH, backups): ")
            # Prompt específico para cumplir requisitos: items, justificación, riesgos
            final_prompt = (
                f"Actúa como experto en sistemas. Genera un checklist técnico sobre: '{tema}'.\n"
                "La salida debe ser en formato Markdown y contener obligatoriamente para cada punto:\n"
                "- El ítem a revisar.\n"
                "- Una justificación corta técnica.\n"
                "- El riesgo de seguridad si no se aplica."
            )

        # --- OPCIÓN 2: PLANTILLA ITIL ---
        elif choice == "2":
            texto = input("Pega el texto de la incidencia o nota: ")
            # Prompt específico para cumplir secciones ITIL
            final_prompt = (
                f"Reescribe el siguiente texto desestructurado en una plantilla formal ITIL.\n"
                f"Texto original: '{texto}'\n\n"
                "Debes usar EXACTAMENTE estas secciones:\n"
                "1. Resumen\n2. Impacto\n3. Urgencia\n4. Acciones\n5. Evidencias\n6. Próximos pasos"
            )

        # --- OPCIÓN 3: RESPUESTA GUIADA ---
        elif choice == "3":
            problema = input("Describe el problema ambiguo (ej. 'la vpn no va'): ")
            # Prompt para forzar preguntas de aclaración antes de la solución
            final_prompt = (
                f"El usuario reporta este problema ambiguo: '{problema}'.\n"
                "NO des la solución definitiva todavía. Tu respuesta debe tener estrictamente:\n"
                "1. Una lista de 3 a 5 preguntas técnicas para aclarar la situación.\n"
                "2. Una primera hipótesis de qué puede estar pasando.\n"
                "3. Un plan de diagnóstico inicial en pasos numerados."
            )

        print("\n⏳ Consultando a la IA... (Espere unos segundos)")
        
        # Llamada modular a la IA
        respuesta = ai_client.call_llm(final_prompt)
        
        print("\n" + "="*40)
        print("RESPUESTA DE LA IA:")
        print("="*40)
        print(respuesta)
        print("="*40)

        # Guardar log
        log_interaction(choice, final_prompt, respuesta)
        print(" Interacción guardada en logs.jsonl")

if __name__ == "__main__":
    main()