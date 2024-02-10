"""CRUD operations for plans."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import selectinload

import api.models.models as models
import api.schemas.plan as plan_schema


async def create_plan(db: AsyncSession, plan: plan_schema.PlanCreate):
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
    result = await db.execute(
        select(models.Plan).options(selectinload(models.Plan.places))
    )
    plans = result.scalars().all()
    return plans
