from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.book import Book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, author: str, year_published: int = None, isbn: str = None, copies_available: int = 1):
    db_book = Book(
        title=title,
        author=author,
        year_published=year_published,
        isbn=isbn,
        copies_available=copies_available
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, title: str, author: str, year_published: int = None, isbn: str = None, copies_available: int = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_book.title = title
    db_book.author = author
    db_book.year_published = year_published
    db_book.isbn = isbn
    if copies_available is not None:
        db_book.copies_available = copies_available

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
