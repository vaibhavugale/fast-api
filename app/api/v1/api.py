from fastapi import APIRouter
from app.api.v1.endpoints import security

api_router = APIRouter()
api_router.include_router(security.router, tags=["login"])
