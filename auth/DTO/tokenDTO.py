from datetime import datetime, timedelta

from pydantic import BaseModel, Field


class SubDTO(BaseModel):
    user_id: int
    username: str


class TokenPayloadDTO(BaseModel):
    exp: datetime
    iat: datetime
    scope: str
    sub: SubDTO
