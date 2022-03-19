from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base


class RoutesPoint(Base):
    __tablename__ = 'routes_points'

    route_id = Column(ForeignKey('route.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    point_id = Column(ForeignKey('point.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    order = Column(Integer, nullable=False)


class RoutePart(RoutesPoint):
    point = relationship('Point')
