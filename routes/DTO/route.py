from typing import List

from pydantic import BaseModel

from DTO import PointDTO


class RouteCreateDTO(BaseModel):
    title: str
    start_point_id: int
    end_point_id: int


class RouteWriteDTO(RouteCreateDTO):
    user_id: int

    @classmethod
    def from_create_dto(cls, create_dto: RouteCreateDTO, user_id):
        return cls(
            title=create_dto.title,
            start_point_id=create_dto.start_point_id,
            end_point_id=create_dto.end_point_id,
            user_id=user_id
        )


class RouteDTO(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        orm_mode = True


class RoutePartDTO(BaseModel):
    point: PointDTO
    order: int

    class Config:
        orm_mode = True


class RouteFullDTO(RouteDTO):
    points: List[RoutePartDTO]

    class Config:
        orm_mode = True
