from models import Task
from sqlalchemy.orm import Session

class TaskRepository:
    def __init__(self,db:Session):
        self.db = db
    def create_task(self,tasko:str):
        newTask = Task(task=tasko)
        self.db.add(newTask)
        self.db.commit()
        self.db.refresh(newTask)
        return newTask
    def set_task(self,task_id:int,task_isdone:bool):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        task.is_done = task_isdone
        self.db.commit()
        self.db.refresh(task)
        return task
    def exists(self, task_id: int = None, task_name: str = None) -> bool:
        query = self.db.query(Task)

        if task_id is not None:
            query = query.filter(Task.id == task_id)

        if task_name is not None:
            query = query.filter(Task.task == task_name)

        return query.first() is not None
    def show_tasks(self):
        return self.db.query(Task).all()
    