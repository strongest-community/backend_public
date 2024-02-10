"""Planのスキーマを定義する"""

from typing import Optional, List
from pydantic import BaseModel, Field
from api.schemas.place import Place, PlaceCreate
from api.schemas.comment import Comment


class PlanBase(BaseModel):
    """PlanBase class は PlanCreate と Plan の共通のフィールドを持つ"""

    title: Optional[str] = Field(..., example="家族旅行")
    description: Optional[str] = Field(None, example="家族で沖縄旅行")
    budget: Optional[int] = Field(None, example=100000)
    situation: Optional[str] = Field(None, example="家族旅行")
    with_whom: Optional[str] = Field(None, example="家族")


class PlanCreate(PlanBase):
    """PlanBaseと同じなのでpass"""

    places: List[PlaceCreate]


class PlanCreateResponse(PlanCreate):
    """PlanCreate のレスポンスモデル"""

    id: int
    places: List[Place] = []

    class Config:
        """Config"""

        orm_mode = True


class Plan(PlanBase):
    """PlanBase と同じなので pass"""

    id: int
    places: List[Place]
    comments: List[Comment]

    class Config:
        """Config"""

        orm_mode = True
