import random
from typing import List

from fastapi import Depends

from DTO import RouteWriteDTO
from models import RoutePart, RouteWithPoints
from services import PointService
from services.route import RouteService


class RouteGenerator:

    def __init__(
            self,
            route_service: RouteService = Depends(RouteService),
            point_service: PointService = Depends(PointService)
    ):
        self.rout_service = route_service
        self.point_service = point_service

    def _generate_random_points_ids(self, existing_points_ids: List[int]) -> List[int]:
        generated_ids: List[int] = []
        for i in range(2, random.choice(range(2, 100))):
            try:
                generated_id = existing_points_ids.pop(
                    random.choice(
                        range(0, len(existing_points_ids))
                    )
                )
                generated_ids.append(generated_id)
            except IndexError:
                break
        return generated_ids

    def create_route(self, route_dto: RouteWriteDTO) -> RouteWithPoints:

        points = self.point_service.get_without_ids([route_dto.start_point_id, route_dto.end_point_id])
        points_ids = list(map(lambda point: point.id, points))
        generated_points_ids = self._generate_random_points_ids(points_ids)

        route_parts: List[RoutePart] = []

        order = 1
        route_parts.append(RoutePart(point_id=route_dto.start_point_id, order=order))
        order += 1
        for point_id in generated_points_ids:
            route_part = RoutePart(point_id=point_id, order=order)
            route_parts.append(route_part)
            order += 1

        route_parts.append(RoutePart(point_id=route_dto.end_point_id, order=order))

        return self.rout_service.create(route_dto.title, route_dto.user_id, route_parts)
