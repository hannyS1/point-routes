from sqlalchemy import or_, and_, not_
from typing import Optional, TypeVar, Callable, Generic

from fastapi import Depends
from dataclasses import dataclass
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BooleanClauseList

from config.database import Base, SessionLocal
from models import Route
from utils.database import get_db


from abc import ABC, abstractmethod
from typing import Any


T = TypeVar("T", bound=Base)


class BaseSpecification(ABC):

    @abstractmethod
    def get_criteria(self) -> BooleanClauseList:
        raise NotImplementedError()

    def And(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def Or(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)

    def Not(self) -> "NotSpecification":
        return NotSpecification(self)


class ISpecification(BaseSpecification, ABC, Generic[T]):
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_query(self):
        self.db.query(T).filter(self.get_criteria())


@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return and_(self.first.get_criteria(), self.second.get_criteria())


@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return or_(self.first.get_criteria(), self.second.get_criteria())


@dataclass(frozen=True)
class NotSpecification(BaseSpecification):
    subject: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return not_(self.subject.get_criteria())








@dataclass(frozen=True)
class RouteByTitleSpecification(BaseSpecification):
    title: str

    def get_criteria(self) -> BooleanClauseList:
        return Route.title == self.title


@dataclass(frozen=True)
class RouteByUserIdSpecification(BaseSpecification):
    user_id: int

    def get_criteria(self) -> BooleanClauseList:
        return Route.user_id == self.user_id


# def find_route(db: Session = Depends(get_db), user_id: Optional[int] = None, title: Optional[str] = None):
#     return db.query(Route).filter()
