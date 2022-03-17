from typing import List

from fastapi import APIRouter

from DTO import UserDTO
from services import UserService

user_router = APIRouter(prefix='/api/users')
user_service = UserService()


@user_router.get('', response_model=List[UserDTO])
async def get_all():
    users = user_service.get_all()
    return users


@user_router.get('/{user_id}', response_model=UserDTO)
async def get_by_id(user_id: int):
    user = user_service.get_by_id(user_id)
    return user
