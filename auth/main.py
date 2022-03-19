from fastapi import FastAPI

from routers.jwt_auth import jwt_router
from routers.user import user_router
from config.openapi import OPENAPI_SCHEMA, OPENAPI_URL

app = FastAPI(
    docs_url='/docs',
    openapi_url=OPENAPI_URL
)

app.include_router(jwt_router)
app.include_router(user_router)


def custom_schema():
    app.openapi_schema = OPENAPI_SCHEMA
    return app.openapi_schema


app.openapi = custom_schema
