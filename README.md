# Projecto: Api FastAPI

API, desarrollada con FastAPI, para la gestión de tareas.

# Caracteristicas del Proyecto
### Version de Python: 3.12
### Version de FastAPI: 0.114.0
### Version de Uvicorn: 0.30.6
### Linter Flake8

# Como iniciar el proyecto en local

Primero clona el repositorio en tu maquina local.
```bash
git clone https://github.com/islas333/fastapi_todolist.git
```

Te recomiendo crear un ambiente virtual para instalar las dependencias del proyecto.

# Instalación de venv Python 
para instalar el entorno virtual de python, se debe ejecutar el siguiente comando en la terminal.
```bash
python -m venv venv
```

Ya que tienes el proyecto en tu maquina local, debes instalar las dependencias necesarias para ejecutar el proyecto.

# Instalación de librerias
para instalar las librerias necesarias, se debe ejecutar el siguiente comando en la terminal.
```bash
pip install -r requirements.txt
```

# Ejecutar Proyecto con Uvicorn en local
Para ejecutar el proyecto con Uvicorn, se debe ejecutar el siguiente comando en la terminal.
```bash
uvicorn todolist.main:app --reload
```

# Liter en local
Para ejecutar el linter Flake8, y garantizar que el codigo cumpla con la caracteristicas de flake8, se debe ejecutar el siguiente comando en la terminal.
```bash
flake8 todolist/main.py
```
[flake8]
max-line-length = 88
ignore = E203, E266, E501, W503

# Test en local
Para ejecutar los test, se debe ejecutar el siguiente comando en la terminal.
```bash
pytest
```

# Docker
Para ejecutar el proyecto con Docker, se debe ejecutar el siguiente comando en la terminal.
```bash
docker build -t todolist .
docker run -d --name todolist -p 8000:8000 todolist
```

El proyecto se ejecutara en el puerto 8000, para acceder a la documentación de la API, se debe ingresar a la siguiente url.
```bash
http://127.0.0.1:8000/tasks
```

Podras observar todos los elementos del MOCK generado


# Rutas

el proyecto cuenta con las siguientes rutas de documentación.
```bash
# Documentación
```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

# Mock
Para el proyecto se utiliza un archivo Mock con datos de prueba, el json generado con https://www.mockaroo.com/ y se almacena en un archivo json de la carpeta todolist/data.


### Endpoints del API:
- GET /: Devuelve una respuesta JSON con una clave "message" establecida en "Hola Mundo".
- GET /mock-data: Devuelve los datos simulados cargados desde el archivo MOCK_DATA.json.
- GET /tasks: Devuelve una respuesta JSON con todas las tareas.
- POST /tasks: Crea una nueva tarea con los datos proporcionados.
- GET /tasks/{task_id}: Devuelve la tarea con el task_id especificado.
- PUT /tasks/{task_id}: Actualiza la tarea con el task_id especificado.
- DELETE /tasks/{task_id}: Elimina la tarea con el task_id especificado.

### Clases:
- Task: Representa una tarea con id, título, descripción y estado de completado.

### Constantes:
- MOCK_DATA_FILE: La ruta del archivo JSON que contiene los datos simulados.
- MOCK_DATA: La lista de tareas cargadas desde MOCK_DATA.json.

## Pendiente: Actualizar API con GraphQL y Strawberry V2

Para mejorar la API y aprovechar las ventajas de GraphQL, se actualizará a la versión 2 usando Strawberry. Esta actualización permitirá mejorar tanto la API como la documentación asociada.
