from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import Book, BookCreate
from app.services.book import get_books, get_book, create_book, update_book, delete_book

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_books(db)

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=Book, status_code=201)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, **book.dict())

@router.put("/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    updated = update_book(db, book_id, **book.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    delete_book(db, book_id)
    return {"detail": "Book deleted"}
