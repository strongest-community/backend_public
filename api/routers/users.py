from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.users as db_user
from api.db import get_db
from api.schemas.user import UserCreate, UserDisplay


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=UserDisplay)
async def create_user(request: UserCreate, db: AsyncSession = Depends(get_db)):
    return await db_user.create_user(db, request)
