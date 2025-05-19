from pydantic import BaseModel
from typing import Optional

class BorrowedBookBase(BaseModel):
    book_id: int
    reader_id: int

class BorrowedBookCreate(BorrowedBookBase):
    pass

class BorrowedBook(BorrowedBookBase):
    id: int
    borrow_date: str
    return_date: Optional[str]

    class Config:
        orm_mode = True
