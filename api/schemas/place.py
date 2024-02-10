"""Placeのスキーマを定義する """

from pydantic import BaseModel, Field


class PlaceBase(BaseModel):
    """PlaceBase class"""

    place_id: int = Field(..., example=123)
    url: str = Field(..., example="http://example.com/place")


class PlaceCreate(PlaceBase):
    """PlaceCreate"""

    pass


class Place(PlaceBase):
    """Place"""

    id: int

    class Config:
        """Config"""

        orm_mode = True
