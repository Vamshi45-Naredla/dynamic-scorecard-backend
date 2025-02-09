from pydantic import BaseModel
from typing import List

class ScoreEntry(BaseModel):
    name: str
    category: str
    score: float

class ScoreData(BaseModel):
    entries: List[ScoreEntry]
