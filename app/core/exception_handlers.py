from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import TaskNotFoundException , UserNotFoundException


async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Task not found"
        }
    )
    
    
async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={"detail": "User not found"}
    )