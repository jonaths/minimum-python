# Proyecto mínimo de Python

## Características

1. Directorio tests configurado para probar y leer archivos desde el directorio app/ 
2. Archivo config.py para leer variables de ambiente desde un archivo .env en el root
3. Archivo .gitignore
4. Archivo requirements.txt con librería rich (para imprimir en la consola) y python-dotenv (para cargar variables de ambiente desde el archivo .env)
5. Dockerfile para construir un contenedor que instala las librerías necesarias usando virtualenv

## Instalación
1. Crear virtualenv `virtualenv env --python=python3`
2. Instalar requerimientos `pip install -r requirements.txt`