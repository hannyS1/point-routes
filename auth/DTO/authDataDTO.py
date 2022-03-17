from pydantic import BaseModel


class AuthDataDTO(BaseModel):
    username: str
    password: str
