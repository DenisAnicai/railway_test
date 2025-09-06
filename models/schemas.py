from pydantic import BaseModel
from datetime import datetime
from typing import List

class NoteCreate(BaseModel):
    content: str
    author: str

class NoteResponse(BaseModel):
    id: int
    content: str
    timestamp: datetime
    author: str
    
    class Config:
        from_attributes=True

class NotesListResponse(BaseModel):
    notes: List[NoteResponse]