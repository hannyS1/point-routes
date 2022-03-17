from typing import List

from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status

from models import User
from utils.database import session


class UserService:

    def __init__(self):
        self.hasher = CryptContext(schemes=['sha256_crypt'])

    @session
    def get_all(self, db: Session) -> List[User]:
        return db.query(User).all()

    @session
    def get_by_id(self, db: Session, user_id: int) -> User:
        user: User = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return user

    @session
    def create_user(self, db: Session, username: str, password: str) -> User:
        hashed_password = self.hasher.hash(password)
        user = User(username=username, password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @session
    def authenticate_user(self, db: Session, username: str, password: str) -> User:
        user: User = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid username')
        if not self.hasher.verify(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

        return user



