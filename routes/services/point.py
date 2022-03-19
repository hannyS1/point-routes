from typing import List

from sqlalchemy.orm import Session, Query
from fastapi import HTTPException, Depends
from starlette import status

from DTO import PointCreateDTO
from models import Point
from utils.database import get_db


class PointService:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    @property
    def default_query(self) -> Query:
        return self.db.query(Point).filter(Point.deleted == False)

    def get_all(self, limit: int, offset: int) -> List[Point]:
        return self.default_query.offset(offset).limit(limit).all()

    def get_by_id(self, point_id: int) -> Point:
        point = self.db.query(Point).filter(Point.id == point_id).first()
        if not point:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return point

    def get_by_ids(self, points_ids: List[int]):
        points = self.default_query.filter(Point.id.in_(points_ids)).all()
        return points

    def get_without_ids(self, points_ids: List[int]) -> List[Point]:
        points = self.default_query.filter(~Point.id.in_(points_ids)).all()
        return points

    def create_point_instance(self, point_dto: PointCreateDTO) -> Point:
        return Point(
            title=point_dto.title,
            latitude=point_dto.latitude,
            longitude=point_dto.longitude,
        )

    def create_point(self, point_dto: PointCreateDTO) -> Point:
        point = self.create_point_instance(point_dto)
        self.db.add(point)
        self.db.commit()
        self.db.refresh(point)
        return point

    def create_points(self, points: List[Point]):
        self.db.add_all(points)
        self.db.commit()
        self.db.refresh(points)
        return points

    def safe_delete(self, point_id: int):
        self.db.query(Point).filter(Point.id == point_id).update({Point.deleted: True})
        self.db.commit()
