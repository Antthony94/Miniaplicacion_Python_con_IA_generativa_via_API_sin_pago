# 📘 Miniaplicación Python con IA Generativa (ASIR)

## 1. Introducción y Objetivo

El objetivo de esta práctica es desarrollar una **aplicación de consola (CLI) en Python** para la asignatura de **Administración de Sistemas Informáticos en Red (ASIR)**. La aplicación actúa como un **asistente técnico**, capaz de resolver tareas habituales de administración de sistemas mediante el uso de **IA generativa**.

Para ello, se integra la **API de Google Gemini**, utilizando exclusivamente el **Free Tier**, cumpliendo los requisitos de:

* Seguridad (protección de la API Key)
* Modularidad del código
* Registro de actividad (logging)
* Buenas prácticas profesionales

---

## 2. Descripción General del Proyecto

Se trata de una miniaplicación en modo texto que permite al usuario interactuar con un modelo de IA para:

* Generar checklists técnicos
* Transformar texto técnico en informes profesionales (ITIL)
* Guiar la resolución de problemas sin dar respuestas directas

La aplicación está diseñada para ser **simple de ejecutar**, **fácil de entender**.

---

## 3. Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Proveedor de IA:** Google Gemini API
* **Modelo:** `gemini-flash-latest`
* **Librerías:**

  * `google-generativeai`
  * `python-dotenv`

---

## 4. Estructura del Proyecto

```
/miniapp-ia-asir
│── main.py
│── ai_client.py
│── requirements.txt
│── .env.example
│── logs.jsonl
```

---

## 5. Configuración y Ejecución

### 5.1 Instalación de Dependencias

```bash
pip install -r requirements.txt
```

Esto instala todas las librerías necesarias para que el proyecto funcione correctamente.

---

### 5.2 Configuración Segura de la API Key

1. Obtener la **API Key** desde **Google AI Studio**.
2. Renombrar el archivo:

```
.env.example → .env
```

3. Editar el archivo `.env` y añadir:

```
GOOGLE_API_KEY=TU_API_KEY_AQUÍ
```

---

### 5.3 Ejecución del Programa

```bash
python main.py
```

Esto lanza la aplicación y muestra el menú interactivo en consola.

---

## 6. Desarrollo Paso a Paso (Proceso Real)

### 6.1 Preparación del Entorno

* Se crea (opcionalmente) un entorno virtual.
* Se instalan las dependencias definidas en `requirements.txt`.

Motivo: aislar el proyecto y evitar conflictos de versiones.

---

### 6.2 Seguridad de la API Key

Decisión clave del proyecto:

* **Nunca escribir la API Key en el código**.
* Uso de variables de entorno mediante `python-dotenv`.

Esto replica un estándar profesional real.

---

### 6.3 Desarrollo del Cliente de IA (`ai_client.py`)

Este archivo se encarga exclusivamente de **hablar con Google Gemini**.

Funciones clave:

* Cargar la API Key desde el entorno.
* Configurar el modelo `gemini-flash-latest`.
* Limitar tokens para controlar el coste.
* Añadir `time.sleep(2)` para evitar errores **429 (Rate Limit)**.
* Manejar errores con `try...except` para que el programa no se bloquee.

Separar esta lógica mejora la limpieza y mantenibilidad del proyecto.

---

### 6.4 Desarrollo del Programa Principal (`main.py`)

Este archivo actúa como:

* Interfaz con el usuario
* Controlador del flujo del programa

Incluye:

* Menú infinito con `while True`
* Varias opciones funcionales
* Ingeniería de prompts (prompt engineering)
* Sistema de logs

El programa solo termina cuando el usuario decide salir.

---

### 6.5 Ingeniería de Prompts

Cada opción del menú envía **instrucciones precisas** a la IA:

* **Checklist técnico:** salida estructurada en Markdown, con riesgos y justificación.
* **Informe ITIL:** transformación de texto desordenado en documento profesional.
* **Respuesta guiada:** la IA no da la solución directa, primero hace preguntas.

Esto reduce errores y mejora la calidad de las respuestas.

---

### 6.6 Depuración y Problemas Reales

Durante el desarrollo surgieron errores importantes:

* El modelo `gemini-1.5-flash` devolvía error 404.
* Se creó un script de diagnóstico (`test_models.py`) para listar modelos disponibles.
* Solución final: uso del alias estable `gemini-flash-latest`.



---

## 7. Análisis Técnico: Archivo por Archivo

### 📂 requirements.txt

Contenido:

```
google-generativeai
python-dotenv
```

* Define todas las dependencias del proyecto.
* Permite replicar el entorno fácilmente.

---

### 📂 .env (NO SUBIR A GITHUB)

* Contiene la API Key real.
* Git debe ignorarlo mediante `.gitignore`.

Es la "caja fuerte" del proyecto.

---

### 📂 .env.example

* Plantilla pública del archivo `.env`.
* Indica qué variables son necesarias para ejecutar el programa.

Estándar profesional de la industria.

---

### 📂 ai_client.py

* Encapsula toda la lógica de conexión con Gemini.
* Gestiona errores y límites.
* Devuelve respuestas limpias al programa principal.

Es el intermediario entre Python y la IA.

---

### 📂 main.py

* Controla el menú y la interacción con el usuario.
* Aplica prompt engineering.
* Registra toda la actividad en logs.

Es el "cerebro" de la aplicación.

---

### 📂 logs.jsonl

* Archivo de evidencia de ejecución.
* Cada línea es un JSON válido (formato JSONL).

---

## 8. Conclusión

Esta práctica demuestra:

* Uso realista de IA generativa
* Aplicación de buenas prácticas de seguridad
* Diseño modular y profesional
* Capacidad de depuración y análisis técnico


