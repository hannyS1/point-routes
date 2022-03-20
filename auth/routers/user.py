from typing import List

from fastapi import APIRouter, Depends
from fastapi.params import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from DTO import UserDTO
from services import UserService, JWTAuthService

user_router = APIRouter(prefix='/api/users')
bearer = HTTPBearer()


@user_router.get('', response_model=List[UserDTO])
async def get_all(user_service: UserService = Depends(UserService)):
    users = user_service.get_all()
    return users


@user_router.get('/me', response_model=UserDTO)
async def me(
        credentials: HTTPAuthorizationCredentials = Security(bearer),
        user_service: UserService = Depends(UserService),
        jwt_service: JWTAuthService = Depends(JWTAuthService)
):
    token = credentials.credentials
    user_id = jwt_service.decode_token(token).user_id
    return user_service.get_by_id(user_id)


@user_router.get('/{user_id}', response_model=UserDTO)
async def get_by_id(user_id: int, user_service: UserService = Depends(UserService)):
    user = user_service.get_by_id(user_id)
    return user



