from fastapi import APIRouter

from src.app.modules.auth.auth_route import auth_router
from src.app.modules.transaction.transaction_route import transaction_router

ROUTERS = [
    auth_router,
    transaction_router,
]

router = APIRouter()

for module_router in ROUTERS:
    router.include_router(module_router)
