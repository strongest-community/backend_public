"""comment router module"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.comment as comment_schema
import api.cruds.comments as comments_crud
from api.db import get_db

router = APIRouter()


@router.post("/comment/{plan_id}", response_model=comment_schema.CommentCreateResponse)
async def post_comment(
    plan_id: int,
    comment: comment_schema.CommentCreate,
    db: AsyncSession = Depends(get_db),
):
    """comment function"""
    db_comment = await comments_crud.post_comment(db, plan_id, comment)
    return db_comment
