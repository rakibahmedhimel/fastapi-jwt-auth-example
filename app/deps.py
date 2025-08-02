# 📄 app/deps.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.core import security
from app.crud.user import get_user_by_email
from app.schemas.user import UserOut

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> UserOut:
    token_data = security.decode_access_token(token)
    if not token_data or not token_data.email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = get_user_by_email(db, token_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user