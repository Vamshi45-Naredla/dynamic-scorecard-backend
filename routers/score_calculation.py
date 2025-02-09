from fastapi import APIRouter
from database import fake_db  # Import in-memory storage
from models import ScoreData

router = APIRouter()

@router.get("/calculate_scores")
async def calculate_scores():
    total_score = sum(entry.score for entry in fake_db)  # Calculate total
    return {"message": "Scores calculated successfully", "total_score": total_score}
