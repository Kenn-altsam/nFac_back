from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskRead(TaskCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True