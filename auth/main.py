from fastapi import FastAPI


from routers.jwt_auth import jwt_router
from routers.user import user_router

app = FastAPI(docs_url='/api/docs')

app.include_router(jwt_router)
app.include_router(user_router)
