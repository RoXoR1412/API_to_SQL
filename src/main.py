from fastapi import FastAPI, HTTPException, Depends, status
from contextlib import asynccontextmanager
import requests
from api.events.routing import router as events_router
from api.db.create import init_db
from dotenv import load_dotenv
import os
from pprint import pprint
from fastapi.responses import JSONResponse

load_dotenv()
API_URL=os.environ.get("API_URL")
API_KEY=os.environ.get("API_KEY")
API_HOST=os.environ.get("API_HOST")

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app=FastAPI(lifespan=lifespan)
# app=FastAPI()
app.include_router(events_router, prefix="/sql")

@app.get("/")
def show_root():
    return {"message": "Welcome to the FastAPI application!"}