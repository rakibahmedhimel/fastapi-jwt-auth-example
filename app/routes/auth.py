# 📄 app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserOut, Token
from app.crud.user import get_user_by_email, create_user
from app.core.security import verify_password, create_access_token
from app.deps import get_db, get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_current_user(current_user: UserOut = Depends(get_current_user)):
    return current_user
