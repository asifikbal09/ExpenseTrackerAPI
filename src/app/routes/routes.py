from fastapi import APIRouter

from src.app.modules.auth.auth_route import auth_router

ROUTERS = [
    auth_router,
]

router = APIRouter()

for module_router in ROUTERS:
    router.include_router(module_router)
