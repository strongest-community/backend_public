"""models.py"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Plan(Base):
    """Plan model"""

    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(String(512))
    budget = Column(Integer)
    situation = Column(String(256))
    with_whom = Column(String(256))

    places = relationship("Place", back_populates="plan")
    comments = relationship("Comment", back_populates="plan")


class Place(Base):
    """Place model"""

    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    url = Column(String(1024))

    plan = relationship("Plan", back_populates="places")


class Comment(Base):
    """Comment model"""

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    comment = Column(String(140))
    stars = Column(Integer)
    plan = relationship("Plan", back_populates="comments")
