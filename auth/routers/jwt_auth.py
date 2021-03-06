from fastapi import APIRouter, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.responses import JSONResponse

from DTO import AuthDataDTO, SubDTO
from services import UserService, JWTAuthService

jwt_router = APIRouter(prefix='/api/jwt')

jwt_service = JWTAuthService()

bearer = HTTPBearer()


@jwt_router.post('/signin')
async def signin(auth_data: AuthDataDTO, user_service: UserService = Depends(UserService)):
    user = user_service.authenticate_user(auth_data.username, auth_data.password)
    return jwt_service.encode_tokens(SubDTO(
        user_id=user.id,
        username=user.username,
    ))


@jwt_router.post('/signup')
async def signup(auth_data: AuthDataDTO, user_service: UserService = Depends(UserService)):
    user = user_service.create_user(auth_data.username, auth_data.password)
    return jwt_service.encode_tokens(SubDTO(
        user_id=user.id,
        username=user.username
    ))


@jwt_router.get('/refresh')
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(bearer)):
    refresh_token = credentials.credentials
    new_token = jwt_service.refresh_token(refresh_token)
    return {'access_token': new_token}


@jwt_router.get('/check-auth')
async def check_auth_middleware(credentials: HTTPAuthorizationCredentials = Security(bearer)):
    token = credentials.credentials
    sub = jwt_service.decode_token(token)
    return JSONResponse(headers={'user-id': str(sub.user_id)})
