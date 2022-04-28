from fastapi import FastAPI
from models import *
from routes.tren import tren


from dotenv import dotenv_values
import os

app = FastAPI(title="FastAPI & Mongo CRUD",
  description="this is a simple REST API using fastapi and mongodb",
  version="0.0.1"
)

app.include_router(tren)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

    
