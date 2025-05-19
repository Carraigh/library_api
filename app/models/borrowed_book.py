from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database import Base

class BorrowedBook(Base):
    __tablename__ = "borrowed_books"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    reader_id = Column(Integer, ForeignKey("readers.id"))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
