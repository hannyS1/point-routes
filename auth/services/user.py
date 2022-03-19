from typing import List

from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status

from config.database import SessionLocal
from models import User
from utils.database import get_db


class UserService:

    def __init__(self, db: Session = Depends(get_db)):
        self.hasher = CryptContext(schemes=['sha256_crypt'])
        self.db = db

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User:
        user: User = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return user

    def create_user(self, username: str, password: str) -> User:
        hashed_password = self.hasher.hash(password)
        user = User(username=username, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate_user(self, username: str, password: str) -> User:
        user: User = self.db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid username')
        if not self.hasher.verify(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

        return user



