from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth import register_user, authenticate_user
from app.schemas.auth import UserCreate, Token
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    return authenticate_user(db, email, password)
