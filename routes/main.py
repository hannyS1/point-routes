from fastapi import FastAPI

from routers.point import point_router
from routers.route import route_router
from config.openapi import OPENAPI_SCHEMA, OPENAPI_URL

app = FastAPI(
    docs_url='/docs',
    openapi_url=OPENAPI_URL,
)

app.include_router(point_router)
app.include_router(route_router)


def custom_schema():
    app.openapi_schema = OPENAPI_SCHEMA
    return app.openapi_schema


app.openapi = custom_schema
