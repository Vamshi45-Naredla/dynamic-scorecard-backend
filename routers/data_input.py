from fastapi import APIRouter
from models import ScoreData
from database import fake_db  # Import in-memory storage

router = APIRouter()

@router.post("/add_scores")
async def add_scores(data: ScoreData):
    fake_db.extend(data.entries)  # Store data in memory
    return {"message": "Scores added successfully"}

@router.get("/get_scores")
async def get_scores():
    return {"message": "Scores retrieved successfully", "data": fake_db}
