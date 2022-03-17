import os
from datetime import timedelta, datetime
from typing import Dict

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from starlette import status

from DTO import TokenPayloadDTO, SubDTO


class JWTAuthService:

    def __init__(self):
        self.secret_key = os.environ.get('AUTH_SECRET_KEY', 'SECRET_KEY')

    def encode_token(self, sub: SubDTO) -> str:
        payload = TokenPayloadDTO(
            scope='access_token',
            sub=sub
        )
        return jwt.encode(payload.dict(), self.secret_key, algorithm='HS256')

    def decode_token(self, token: str) -> SubDTO:
        try:
            payload_dict = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            payload = TokenPayloadDTO.parse_obj(payload_dict)
            if payload.scope != 'access_token':
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid scope')
            return SubDTO.parse_obj(payload.sub)

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token')

    def encode_refresh_token(self, sub: SubDTO) -> str:
        payload: TokenPayloadDTO = TokenPayloadDTO(
            exp=datetime.utcnow() + timedelta(days=1),
            scope='refresh_token',
            sub=sub
        )
        return jwt.encode(payload.dict(), self.secret_key, algorithm='HS256')

    def encode_tokens(self, sub: SubDTO) -> Dict[str, str]:
        return {
            'access_token': self.encode_token(sub),
            'refresh_token': self.encode_refresh_token(sub)
        }

    def refresh_token(self, refresh_token: str) -> str:
        try:
            payload_dict = jwt.decode(refresh_token, self.secret_key, algorithms=['HS256'])
            payload: TokenPayloadDTO = TokenPayloadDTO.parse_obj(payload_dict)
            if payload.scope != 'refresh_token':
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid scope')
            token = SubDTO(
                user_id=payload.sub.user_id,
                username=payload.sub.username
            )
            return self.encode_token(token)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='refresh token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid refresh token')

