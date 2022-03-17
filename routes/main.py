from fastapi import FastAPI

from routers.point import point_router

app = FastAPI(docs_url='/api/docs')

app.include_router(point_router)
