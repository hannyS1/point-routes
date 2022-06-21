from operator import or_

from sqlalchemy import not_
from sqlalchemy.orm import Session

from config.database import SessionLocal
from models import Route
from repository.base_specification import RouteByTitleSpecification, RouteByUserIdSpecification, AndSpecification
from utils.database import get_db


class RouteRepo:

    def test_query(self):
        db: Session = SessionLocal()

        specification_title = RouteByTitleSpecification(title="radas")
        specification_user_id = RouteByUserIdSpecification(user_id=1)

        specification = specification_title.And(specification_user_id.Not())

        query = db.query(Route).filter(specification.get_criteria())

        db.close()

        return query


def main():
    repo = RouteRepo()
    a = repo.test_query()
    print(a)


if __name__ == "__main__":
    main()
