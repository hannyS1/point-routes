from pydantic.main import BaseModel


class PointCreateDTO(BaseModel):
    title: str
    latitude: float
    longitude: float


class PointDTO(BaseModel):
    id: int
    title: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class PointFullDTO(PointDTO):
    deleted: bool
