from datetime import datetime, timedelta

from pydantic import BaseModel, Field


class SubDTO(BaseModel):
    user_id: int
    username: str


class TokenPayloadDTO(BaseModel):
    exp: datetime = Field(default=datetime.utcnow() + timedelta(days=0, hours=1))
    iat: datetime = Field(default=datetime.utcnow())
    scope: str
    sub: SubDTO
