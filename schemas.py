from pydantic import BaseModel,Field

class TaskCreate(BaseModel):
    task:str = Field(min_length=3)

class TaskSet(BaseModel):
    id:int
    is_done:bool

class TaskResponse(BaseModel):
    id:int
    task:str
    is_done:bool

    class Config:
        from_attributes = True