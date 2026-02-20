from database import Base
from sqlalchemy import Column, String,Integer,Boolean

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True)
    task = Column(String,unique=True,nullable=False)
    is_done = Column(Boolean,default=False)