from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import Base,SessionLocal,engine
from schemas import TaskCreate, TaskResponse, TaskSet
from repository import TaskRepository
from service import TaskService

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_service(db:Session = Depends(get_db)):
    repo = TaskRepository(db)
    return TaskService(repo)



@app.get("/tasks",response_model=list[TaskResponse])
def tasks(service = Depends(get_service)):
    return service.query_all()

@app.post("/task",response_model=TaskResponse)
def add_task(tasko:TaskCreate,service = Depends(get_service)):
    return service.add(tasko)

@app.post("/update/task",response_model=TaskResponse)
def update_task(tasko:TaskSet,service= Depends(get_service)):
    return service.setTask(tasko)