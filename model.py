from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Task(BaseModel):
    id:Optional[UUID] =None
    title:str
    desctiprion:Optional[str]
    completed:bool = False


tasks = []

#create tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task


#get all the tasks

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return tasks

#get a specific tasks

@app.get("/tasks/{task_id}", responce_model=Task)
def getaspecifitask(task_id, UUID):
    for task in tasks:
        if task_id == task_id:
            return task
    return HTTPException(status_code=404, detail="tasks not found")


#update a tasks
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id:UUID, task_update:Task):
    for idx , task in enumerate(tasks):
        if task.id ==task_id:
            updated_task =task.copy(update=task_update)
            tasks[idx] = updated_task
            return updated_task
    return HTTPException(status_code=404, detail="task not found")





#delete a task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id:UUID):
    for idx, task in enumerate(tasks):
        if task.id ==task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404, detail="task not found")