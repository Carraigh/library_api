from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.borrowed_book import BorrowedBook
from app.models.book import Book
from app.models.reader import Reader

def borrow_book(db: Session, book_id: int, reader_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.copies_available <= 0:
        raise HTTPException(status_code=400, detail="No available copies")

    reader_borrowed_count = db.query(BorrowedBook).filter(
        BorrowedBook.reader_id == reader_id, BorrowedBook.return_date.is_(None)
    ).count()
    if reader_borrowed_count >= 3:
        raise HTTPException(status_code=400, detail="Reader already has 3 borrowed books")

    db_borrow = BorrowedBook(book_id=book_id, reader_id=reader_id)
    book.copies_available -= 1
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def return_book(db: Session, book_id: int, reader_id: int):
    borrow = db.query(BorrowedBook).filter(
        BorrowedBook.book_id == book_id,
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date.is_(None)
    ).first()
    if not borrow:
        raise HTTPException(status_code=400, detail="Book not borrowed by this reader")

    book = db.query(Book).filter(Book.id == book_id).first()
    book.copies_available += 1
    borrow.return_date = datetime.utcnow()
    db.commit()
    db.refresh(borrow)
    return borrow

def get_borrowed_books_by_reader(db: Session, reader_id: int):
    return db.query(BorrowedBook).filter(BorrowedBook.reader_id == reader_id, BorrowedBook.return_date.is_(None)).all()
