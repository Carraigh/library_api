from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    copies_available: int = 1
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
