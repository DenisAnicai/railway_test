from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.database import get_db, Note
from models.schemas import NoteCreate, NoteResponse, NotesListResponse
from pydantic import BaseModel

router = APIRouter()

@router.get("/notes", response_model=NotesListResponse)
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).order_by(Note.timestamp.desc()).all()
    note_responses = [NoteResponse.model_validate(note) for note in notes]
    return NotesListResponse(notes=note_responses)


@router.post("/note", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(content=note.content, author=note.author)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note