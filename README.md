# Projecto: Api FastAPI

Se desarrolla un API, con flastAPI, para la gestión de usuarios.

### Version de Python: 3.12
### Version de FastAPI: 0.114.0
### Version de Uvicorn: 0.30.6
### Linter Flake8

# Instalación de venv Python 
para instalar el entorno virtual de python, se debe ejecutar el siguiente comando en la terminal.
```bash
python -m venv venv
```


# Instalación de librerias
para instalar las librerias necesarias, se debe ejecutar el siguiente comando en la terminal.
```bash
pip install -r requirements.txt
```

# Ejecutar Proyecto con Uvicorn
Para ejecutar el proyecto con Uvicorn, se debe ejecutar el siguiente comando en la terminal.
```bash
uvicorn todolist.main:app --reload
```

# Liter
Para ejecutar el linter Flake8, se debe ejecutar el siguiente comando en la terminal.
```bash
flake8 todolist/main.py
```

# Test

# Rutas

### Ruta de la documentación

# Documentación
```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

# Mock
Se generan datos de prueba, un json generado en https://www.mockaroo.com/ y se almacena en un archivo json.
```bash
http://127.0.0.1:8000/mock-data
```

### Endpoints:
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