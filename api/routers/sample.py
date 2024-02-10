"""sample router module"""

from fastapi import APIRouter, Depends
from api.auth.auth2 import get_current_user

router = APIRouter()


@router.get("/hello")
async def hello(
    _: str = Depends(get_current_user),
):
    """hello function"""
    return {"message": "hello FastAPI!"}
