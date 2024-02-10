"""CRUD operations for places."""
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.models as models
import api.schemas.place as place_schema


async def create_place(db: AsyncSession, plan_id: int, plan: place_schema.PlaceCreate):
    """Create a place for a plan."""
    dp_place = models.Place(plan_id=plan_id, url=plan.url)
    db.add(dp_place)

    await db.commit()
    await db.refresh(dp_place)

    return dp_place
