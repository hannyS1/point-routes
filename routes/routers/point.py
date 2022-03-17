from typing import List

from fastapi import APIRouter
from starlette.responses import Response
from starlette import status

from DTO import PointCreateDTO, PointDTO, PointFullDTO
from services import PointService

point_router = APIRouter(prefix='/api/points')
point_service = PointService()


@point_router.get('', response_model=List[PointDTO])
async def get_all():
    points = point_service.get_all()
    return points


@point_router.get('/{point_id}', response_model=PointFullDTO)
async def get_by_id(point_id: int):
    point = point_service.get_by_id(point_id)
    return point


@point_router.post('', response_model=PointCreateDTO)
async def create(point_dto: PointCreateDTO):
    point = point_service.create_point(point_dto)
    return point


@point_router.delete('/{point_id}')
async def delete(point_id):
    point_service.safe_delete(point_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
