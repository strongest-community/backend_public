"""Commentのスキーマを定義する"""

from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    """Comment base schema"""

    comment: str = Field(..., max_length=140, description="The content of the comment")
    stars: int = Field(
        ..., ge=0, le=5, description="The star rating given with the comment"
    )


class CommentCreate(CommentBase):
    """Comment create schema"""


class CommentCreateResponse(CommentCreate):
    """Comment create response schema"""

    id: int = Field(..., description="The ID of the comment")
    plan_id: int = Field(..., description="The ID of the plan this comment belongs to")

    class Config:
        """Config"""

        orm_mode = True


class Comment(CommentBase):
    """Comment schema"""
