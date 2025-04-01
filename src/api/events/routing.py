from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session, SQLModel
import requests

router=APIRouter()
#get song details
@router.post("/start")
def input_data():
    pass
    