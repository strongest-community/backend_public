"""models.py"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Plan(Base):
    """Plan model"""

    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(512))
    budget = Column(Integer)
    situation = Column(String(256))
    with_whom = Column(String(256))

    places = relationship("Place", back_populates="plan")


class Place(Base):
    """Place model"""

    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    url = Column(String(1024))

    plan = relationship("Plan", back_populates="places")


class User(Base):
    """User model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    mail = Column(String(128))


class PlanCommentRelation(Base):
    """PlanCommentRelation model"""

    __tablename__ = "plan_comment_relation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
    comment = Column(String(140))


class PlanLikeRelation(Base):
    """PlanLikeRelation model"""

    __tablename__ = "plan_like_relation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
