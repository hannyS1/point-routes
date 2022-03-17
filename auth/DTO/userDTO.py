from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
