from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
app = FastAPI()


class Task(BaseModel):
    id:Optional[UUID] = None
    title:str
    description:Optional[str]
    completed:bool = False

tasks = []
#create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

#get all the tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

#get a specific tasks

@app.get("/tasks/{task_id}/", response_model=Task)
def getaspecifictask(task_id: UUID):
    for task in tasks:
        if task_id == task_id:
            return task
    return HTTPException(status_code=404, detail="task not found")



@app.put("/tasks/{task_id}", response_model=Task)
def update_the_task(task_id:UUID, task_update:Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] =updated_task
            return updated_task
        raise HTTPException(status_code=404, detail="tasks not found")


#delete tassks

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id:UUID):
    for idx , task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404, detail="tasks not found")

        







# this line is for executing simple python file
if __name__ == "__main__":

    #we are importin uvicorn
    import uvicorn

    #trigger this
    uvicorn.run(app, host="0.0.0.0", port=8000)