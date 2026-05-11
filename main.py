from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados simulado
tasks = []

# Modelo de dados da tarefa
class Task(BaseModel):
    description: str
    priority: int

# ROTA POST JÁ REALIZADA ANTERIORMENTE
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Tarefa adicionada com sucesso!", "task": task}

# ROTA GET JÁ REALIZADA ANTERIORMENTE
@app.get("/tasks")
def get_tasks():
    return tasks

# NOVA ROTA PUT
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        return {"error": "ID inválido"}

    tasks[task_id] = task
    return {"message": "Tarefa atualizada com sucesso!", "task": task}

# NOVA ROTA DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        return {"error": "ID inválido"}

    tasks.pop(task_id)
    return {"message": "Tarefa excluída com sucesso!"}

