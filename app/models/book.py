from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer)
    isbn = Column(String, unique=True)
    copies_available = Column(Integer, default=1)
    description = Column(String)  # после миграции
