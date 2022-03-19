from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, relation

from config.database import Base


class Route(Base):
    __tablename__ = 'route'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(255))


class RouteWithPoints(Route):
    points = relationship('RoutePart', lazy='joined', order_by='RoutePart.order')
