from models import Route
from repository.base import BaseRepository


class RouteRepository(BaseRepository):

    def get_all(self):
        return self.db.query(Route).all()
