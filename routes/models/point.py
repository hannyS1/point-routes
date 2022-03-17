from sqlalchemy import Column, Integer, String, Float, Boolean

from config.database import Base


class Point(Base):
    __tablename__ = 'routes_point'

    id = Column(
        Integer,
        primary_key=True,
    )
    latitude = Column(
        Float,
        nullable=False,
    )
    longitude = Column(
        Float,
        nullable=False,
    )
    title = Column(
        String(255),
        nullable=False,
    )
    deleted = Column(
        Boolean,
        default=False,
    )
