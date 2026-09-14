
from fastapi import FastAPI
from app.db.database import create_tables
from app.api.routes.task import router 
from app.api.routes.user import userrouter


app=FastAPI()

app.include_router(router)
app.include_router(userrouter)
create_tables()

@app.get('/')
def check_server():
    return {
        "Working":'Done'
            }
    
    