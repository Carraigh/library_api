from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.borrowed_book import BorrowedBook
from app.services.borrowed_book import borrow_book, return_book, get_borrowed_books_by_reader

router = APIRouter(prefix="/borrow", tags=["Borrowing"])

@router.post("/borrow", response_model=BorrowedBook, status_code=201)
def borrow(book_id: int, reader_id: int, db: Session = Depends(get_db)):
    return borrow_book(db, book_id, reader_id)

@router.post("/return")
def return_b(book_id: int, reader_id: int, db: Session = Depends(get_db)):
    return return_book(db, book_id, reader_id)

@router.get("/reader/{reader_id}", response_model=list[BorrowedBook])
def list_borrowed(reader_id: int, db: Session = Depends(get_db)):
    return get_borrowed_books_by_reader(db, reader_id)
