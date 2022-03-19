from typing import List

from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette import status

from DTO import PointCreateDTO, PointDTO, PointFullDTO
from services import PointService

point_router = APIRouter(prefix='/api/points')


@point_router.get('', response_model=List[PointDTO])
async def get_all(
        limit: int = 100,
        offset: int = 0,
        point_service: PointService = Depends(PointService)
):
    points = point_service.get_all(limit, offset)
    return points


@point_router.get('/{point_id}', response_model=PointFullDTO)
async def get_by_id(point_id: int, point_service: PointService = Depends(PointService)):
    point = point_service.get_by_id(point_id)
    return point


@point_router.post('', response_model=PointFullDTO)
async def create(point_dto: PointCreateDTO, point_service: PointService = Depends(PointService)):
    point = point_service.create_point(point_dto)
    return point


@point_router.delete('/{point_id}')
async def delete(point_id: int, point_service: PointService = Depends(PointService)):
    point_service.safe_delete(point_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
