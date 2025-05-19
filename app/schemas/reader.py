from pydantic import BaseModel

class ReaderBase(BaseModel):
    name: str
    email: str

class ReaderCreate(ReaderBase):
    pass

class Reader(ReaderBase):
    id: int

    class Config:
        orm_mode = True
