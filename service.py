from fastapi import HTTPException
from repository import TaskRepository
from schemas import TaskCreate, TaskSet


class TaskService:
    def __init__(self,repo:TaskRepository):
        self.repo = repo
    def add(self,tasko:TaskCreate):
        task_name = tasko.task
        
        if self.repo.exists(task_name=task_name):
            raise HTTPException(
                status_code=400,
                detail="Item already exists"
            )
        return self.repo.create_task(task_name)
    def query_all(self):
        return self.repo.show_tasks()
    def setTask(self,tasko:TaskSet):
        task_id=tasko.id
        task_isdone =tasko.is_done

        if not self.repo.exists(task_id=task_id):
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )
        return self.repo.set_task(task_id=task_id,task_isdone=task_isdone)