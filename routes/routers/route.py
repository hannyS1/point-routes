from typing import List, Optional

from fastapi import APIRouter, Depends, Header
from fastapi.params import Query

from DTO import RouteFullDTO, RouteCreateDTO, RouteDTO, RouteWriteDTO
from services.route import RouteService
from services.route_generator import RouteGenerator

route_router = APIRouter(prefix='/api/routes')


@route_router.get('', response_model=List[RouteDTO])
async def get_all(
        route_service: RouteService = Depends(RouteService),
        user_id: Optional[int] = Query(None)
):
    if user_id:
        return route_service.get_by_user_id(user_id)
    return route_service.get_all()


@route_router.get('/my', response_model=List[RouteDTO])
async def my_routes(
        route_service: RouteService = Depends(RouteService),
        user_id: int = Header(...)
):
    routes = route_service.get_by_user_id(int(user_id))
    return routes


@route_router.get('/{route_id}', response_model=RouteFullDTO)
async def get_by_id(route_id: int, route_service: RouteService = Depends(RouteService)):
    route = route_service.get_by_id(route_id)
    return route


@route_router.post('', response_model=RouteFullDTO)
async def create(
        rout_dto: RouteCreateDTO,
        route_generator: RouteGenerator = Depends(RouteGenerator),
        user_id: int = Header(...)
):
    route_write_dto = RouteWriteDTO.from_create_dto(rout_dto, int(user_id))
    route = route_generator.create_route(route_write_dto)
    return route
