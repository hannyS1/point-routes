from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from DTO import PointCreateDTO
from models import Point
from utils.database import session


class PointService:

    @session
    def get_all(self, db: Session) -> List[Point]:
        return db.query(Point).filter(Point.deleted == False).all()

    @session
    def get_by_id(self, db: Session, point_id: int) -> Point:
        point = db.query(Point).filter(Point.id == point_id).first()
        if not point:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return point

    def create_point_instance(self, point_dto: PointCreateDTO) -> Point:
        return Point(
            title=point_dto.title,
            latitude=point_dto.latitude,
            longitude=point_dto.longitude,
        )

    @session
    def create_point(self, db: Session, point_dto: PointCreateDTO) -> Point:
        point = Point(
            title=point_dto.title,
            latitude=point_dto.latitude,
            longitude=point_dto.longitude,
        )
        db.add(point)
        db.commit()
        db.refresh(point)
        return point

    @session
    def create_points(self, db: Session, points: List[Point]):
        db.add_all(points)
        db.commit()
        db.refresh(points)
        return points

    @session
    def safe_delete(self, db: Session, point_id: int):
        db.query(Point).filter(Point.id == point_id).update({Point.deleted: True})
        db.commit()
