"""CRUD operations for plans."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.models as models
import api.schemas.plan as plan_schema


async def create_plan(db: AsyncSession, plan: plan_schema.PlanCreate):
    db_plan = models.Plan(
        description=plan.description,
        budget=plan.budget,
        situation=plan.situation,
        with_whom=plan.with_whom,
    )
    db.add(db_plan)

    for place_data in plan.places:
        db_place = models.Place(plan_id=db_plan.id, url=place_data.url)
        db.add(db_place)
    await db.commit()
    await db.refresh(db_plan)
    await db.refresh(db_place)

    return db_plan


async def get_all_plans(db: AsyncSession):
    result: Result = await db.execute(
        select(
            models.Plan.id,
            models.Plan.description,
            models.Plan.budget,
            models.Plan.situation,
            models.Plan.with_whom,
            models.Place.url,
        ).outerjoin(models.Place)
    )
    return result.all()
