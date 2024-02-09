"""sample router module"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello():
    """hello function"""
    return {"message": "hello FastAPI!"}
