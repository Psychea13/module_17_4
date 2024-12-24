from fastapi import FastAPI
from app.routers import task, user


app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(task.router_task)
app.include_router(user.router_user)


# uvicorn app.main:app --reload