"""CRUD operations for plans."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.models import models
import api.schemas.plan as plan_schema


async def create_plan(db: AsyncSession, plan: plan_schema.PlanCreate):
    """Create a plan"""
    db_plan = models.Plan(
        title=plan.title,
        description=plan.description,
        budget=plan.budget,
        situation=plan.situation,
        with_whom=plan.with_whom,
    )
    db.add(db_plan)

    await db.commit()
    await db.refresh(db_plan)

    return db_plan


async def get_all_plans(db: AsyncSession):
    """Get all plans."""
    result = await db.execute(
        select(models.Plan).options(
            selectinload(models.Plan.places), selectinload(models.Plan.comments)
        )
    )
    plans = result.scalars().all()
    return plans


async def get_task_by_id(db: AsyncSession, plan_id: int):
    """Get a plan by id."""
    result = await db.execute(
        select(models.Plan)
        .where(models.Plan.id == plan_id)
        .options(selectinload(models.Plan.places))
    )
    plan = result.scalars().first()
    return plan
