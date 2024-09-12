# todolist/services.py
import json
import os
from fastapi import HTTPException
from .models import Task


current_dir = os.path.dirname(os.path.abspath(__file__))
MOCK_DATA_FILE = os.path.join(current_dir, 'data', 'MOCK_DATA.json')
with open(MOCK_DATA_FILE) as f:
    MOCK_DATA = json.load(f)


# @router.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    if not MOCK_DATA or len(MOCK_DATA) == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrados")
    if skip < 0:
        raise HTTPException(status_code=400, detail="El índice de inicio debe ser mayor o igual a 0")
    if limit > len(MOCK_DATA):
        raise HTTPException(status_code=400, detail="El límite es mayor al total de datos")
    total = len(MOCK_DATA)
    return {
        "total_data": total,
        "elemento_ini": skip,
        "elemento_fin": skip + limit - 1,
        "data": MOCK_DATA[skip : skip + limit]
    }


# @router.post("/tasks")
def create_task(task: Task):
    if MOCK_DATA:
        new_id = MOCK_DATA[-1]["id"] + 1
    else:
        new_id = 1
    new_task = task.model_copy(update={"id": new_id})

    MOCK_DATA.append(new_task.model_dump())
    with open(MOCK_DATA_FILE, 'w') as f:
        json.dump(MOCK_DATA, f)
    return {"message": f'Tarea creada satisfactoriamente: id={new_id}'}


# @router.get("/tasks/{task_id}") --
def get_task(task_id: int):
    task = list(filter(lambda t: t["id"] == task_id, MOCK_DATA))
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task[0]


# @router.put("/tasks/{task_id}") --
def update_task(task_id: int, task: Task):
    find_task = list(filter(lambda t: t["id"] == task_id, MOCK_DATA))
    if not find_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    index = MOCK_DATA.index(find_task[0])
    MOCK_DATA[index] = task.model_dump()
    MOCK_DATA[index]['id'] = find_task[0]['id']
    with open(MOCK_DATA_FILE, 'w') as f:
        json.dump(MOCK_DATA, f)
    return {"message": f'Tarea actualizada satisfactoriamente: id={find_task[0]['id']}'}


# @router.delete("/tasks/{task_id}") --
def delete_task(task_id: int):
    find_task = list(filter(lambda t: t["id"] == task_id, MOCK_DATA))
    if not find_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    MOCK_DATA.remove(find_task[0])
    with open(MOCK_DATA_FILE, 'w') as f:
        json.dump(MOCK_DATA, f)
    return {"message": f'Tarea eliminada satisfactoriamente: id={find_task[0]['id']}'}
