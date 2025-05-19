from fastapi import FastAPI
from app.routers import auth, books, readers, borrowed_books

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(readers.router)
app.include_router(borrowed_books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Library API"}
