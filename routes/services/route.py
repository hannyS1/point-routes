from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models import Route, RouteWithPoints, RoutePart
from utils.database import get_db


class RouteService:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, title: str, user_id: int, route_parts: List[RoutePart]) -> RouteWithPoints:
        route = RouteWithPoints(
            title=title,
            user_id=user_id,
            points=route_parts
        )

        self.db.add(route)
        self.db.commit()
        self.db.refresh(route)
        return route

    def get_all(self) -> List[Route]:
        return self.db.query(Route).all()

    def get_by_id(self, route_id: int) -> RouteWithPoints:
        route = self.db.query(RouteWithPoints).get(route_id)
        if not route:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return route

    def get_by_user_id(self, user_id: int) -> List[RouteWithPoints]:
        routes = self.db.query(RouteWithPoints).filter(RouteWithPoints.user_id == user_id).all()
        return routes

