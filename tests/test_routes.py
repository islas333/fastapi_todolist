# tests/test_routes.py
from fastapi.testclient import TestClient
from todolist.main import application

client = TestClient(application)


# validar que el servicio devuelva 10 elementos por defecto
def test_read_tasks_default():
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks['data']) == 10


# validar que el servicio devuelva 5 elementos
def test_read_tasks_with_pagination():
    response = client.get("/tasks?skip=0&limit=5")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks['data']) <= 5


# Validar que se pueda leer una tarea por su id
def test_read_task_by_id():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1


# Validar que se devuelva un error 404 cuando no se encuentra la tarea
def test_read_task_by_id_not_found():
    response = client.get("/tasks/1000")
    assert response.status_code == 404
    error_message = response.json()
    assert "detail" in error_message, "Expected error message to have 'detail'"
    assert error_message["detail"] == "Tarea no encontrada", "Expected specific error message"


# Validar que los datos de la tarea tienen las llaves correctas
def test_read_task_keys():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    task = response.json()
    expected_keys = {"id", "title", "description", "complete"}
    task_keys = set(task.keys())
    assert task_keys == expected_keys, f"Expected keys {expected_keys}, but got {task_keys}"


# Validar que se devuelva un error 422 cuando el id no es un entero
def test_read_task_keys_not_found():
    response = client.get("/tasks/abc")
    assert response.status_code == 422
    error_message = response.json()
    error_message_msg = error_message["detail"][0]['msg']
    assert error_message_msg, "Expected error message to have 'detail'"
    assert error_message_msg == "Input should be a valid integer, unable to parse string as an integer", "Expected specific error message"


# Validar que se pueda crear una tarea
def test_create_task():
    response = client.post("/tasks", json={"title": "string", "description": "Descripción de la tarea", "complete": True})
    assert response.status_code == 200
    message = response.json()
    assert "Tarea creada satisfactoriamente" in message["message"]
    global id_created
    id_created = message["message"]


# validar que se devuelva un error 422 cuando falta el título
def test_create_task_missing_title():
    response = client.post("/tasks", json={"description": "Descripción de la tarea", "complete": True})
    assert response.status_code == 422
    error_message = response.json()
    error_message_msg = error_message["detail"][0]['msg']
    assert error_message_msg, "Expected error message to have 'detail'"
    assert error_message_msg == "Field required", "Expected specific error message"


# validar que se devuelva un error 422 cuando el valor de complete no es un booleano (valor incorrecto)
def test_create_task_incorrect_value():
    response = client.post("/tasks", json={"title": "string", "description": "Descripción de la tarea", "complete": "Sdfsd"})
    assert response.status_code == 422
    error_message = response.json()
    error_message_msg = error_message["detail"][0]['msg']
    assert error_message_msg, "Expected error message to have 'detail'"
    assert error_message_msg == "Input should be a valid boolean, unable to interpret input", "Expected specific error message"


# Validar la actualización de una tarea
def test_update_task():
    response = client.put("/tasks/100", json={"title": "Update test", "description": "Descripcion test", "complete": False})
    assert response.status_code == 200
    message = response.json()
    assert "Tarea actualizada satisfactoriamente" in message["message"]


# Validar que se devuelva un error 404 cuando no se encuentra la tarea
def test_update_task_not_found():
    response = client.put("/tasks/1000", json={"title": "Update test", "description": "Descripcion test", "complete": False})
    assert response.status_code == 404
    error_message = response.json()
    assert "detail" in error_message, "Expected error message to have 'detail'"
    assert error_message["detail"] == "Tarea no encontrada", "Expected specific error message"


# Validar la eliminación de una tarea
def test_delete_task():
    id_delete = id_created.split('=')[1]
    response = client.delete(f'/tasks/{id_delete}')
    assert response.status_code == 200
    message = response.json()
    assert "Tarea eliminada satisfactoriamente" in message["message"]


# Validar que se devuelva un error 404 cuando no se encuentra la tarea
def test_delete_task_not_found():
    response = client.delete("/tasks/100000")
    assert response.status_code == 404
    error_message = response.json()
    assert "detail" in error_message, "Expected error message to have 'detail'"
    assert error_message["detail"] == "Tarea no encontrada", "Expected specific error message"
