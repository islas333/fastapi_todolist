import json
import os
from fastapi import APIRouter
from .services import get_tasks, get_task, create_task, update_task, delete_task
from .models import Task

router = APIRouter()


current_dir = os.path.dirname(os.path.abspath(__file__))
MOCK_DATA_FILE = os.path.join(current_dir, "data", "MOCK_DATA.json")
with open(MOCK_DATA_FILE) as f:
    MOCK_DATA = json.load(f)


@router.get("/tasks")
async def read_tasks(skip: int = 0, limit: int = 10):
    return get_tasks(skip, limit)


@router.post("/tasks")
async def add_task(task: Task):
    return create_task(task)


# ok
@router.get("/tasks/{task_id}")
async def read_task(task_id: int):
    return get_task(task_id)


@router.put("/tasks/{task_id}")
async def modify_task(task_id: int, task: Task):
    return update_task(task_id, task)


@router.delete("/tasks/{task_id}")
async def remove_task(task_id: int):
    return delete_task(task_id)
