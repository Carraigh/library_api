from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.reader import Reader, ReaderCreate
from app.services.reader import get_readers, get_reader, create_reader, update_reader, delete_reader

router = APIRouter(prefix="/readers", tags=["Readers"])

@router.get("/", response_model=list[Reader])
def read_readers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_readers(db)

@router.get("/{reader_id}", response_model=Reader)
def read_reader(reader_id: int, db: Session = Depends(get_db)):
    db_reader = get_reader(db, reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return db_reader

@router.post("/", response_model=Reader, status_code=201)
def create_new_reader(reader: ReaderCreate, db: Session = Depends(get_db)):
    return create_reader(db, **reader.dict())

@router.put("/{reader_id}", response_model=Reader)
def update_existing_reader(reader_id: int, reader: ReaderCreate, db: Session = Depends(get_db)):
    updated = update_reader(db, reader_id, **reader.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Reader not found")
    return updated

@router.delete("/{reader_id}")
def delete_existing_reader(reader_id: int, db: Session = Depends(get_db)):
    delete_reader(db, reader_id)
    return {"detail": "Reader deleted"}
