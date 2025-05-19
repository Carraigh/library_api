from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.reader import Reader

def get_readers(db: Session):
    return db.query(Reader).all()

def get_reader(db: Session, reader_id: int):
    return db.query(Reader).filter(Reader.id == reader_id).first()

def create_reader(db: Session, name: str, email: str):
    db_reader = Reader(name=name, email=email)
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader

def update_reader(db: Session, reader_id: int, name: str, email: str):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    db_reader.name = name
    db_reader.email = email
    db.commit()
    db.refresh(db_reader)
    return db_reader

def delete_reader(db: Session, reader_id: int):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    db.delete(db_reader)
    db.commit()
