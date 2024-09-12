from pydantic import BaseModel, Field
from typing import Optional


class Task(BaseModel):
    id: Optional[int] = Field(default=None, description="ID autoincrementable")
    title: str
    description: str
    complete: bool
