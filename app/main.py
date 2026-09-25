from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.db.database import create_tables
from app.api.routes.task import router 
from app.api.routes.user import userrouter
from fastapi import Request
from fastapi.responses import JSONResponse
import time

from app.core.exceptions import TaskNotFoundException ,UserNotFoundException
from app.core.exception_handlers import task_not_found_handler ,user_not_found_handler


app=FastAPI()

app.add_exception_handler(
    TaskNotFoundException,
    task_not_found_handler
)
    
app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(userrouter)
create_tables()



@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"→ {response.status_code} "
        f"→ {process_time:.4f}s"
    )

    return response
@app.get('/')
def check_server():
    return {
        "Working":'Done'
            }
    
    
