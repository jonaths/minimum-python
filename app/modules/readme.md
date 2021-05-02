# Módulo del proyecto

## Descripción

El objetivo de esta estructura es aislar las funcionalidades de un proyecto por módulos. 
Cada módulo tiene todos los archivos necesarios para funcionar independientemente y puede ser llamado
desde otras partes del código, por ejemplo desde app/. 

## Puntos importantes

- Renombrar module_name de acuerdo a la funcionalidad del módulo (si solo hay una funcionalidad)
- Agregar más carpetas con la misma estructura que module_name de acuerdo conforme se agreguen nuevas funcionalidades
- La idea es que cualquier archivo dentro de la carpeta modules se pueda llamar desde un archivo como main.py en app
