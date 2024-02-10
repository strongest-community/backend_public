from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.plans as plans_crud
import api.schemas.plan as plan_schema
import api.cruds.places as places_crud
from api.db import get_db

router = APIRouter()


@router.get("/plans/", response_model=List[plan_schema.Plan])
async def list_plans(db: AsyncSession = Depends(get_db)):
    """dami-deta function"""
    return await plans_crud.get_all_plans(db)


@router.post("/plans/")
async def create_plan(plan: plan_schema.PlanCreate, db: AsyncSession = Depends(get_db)):
    db_plan = await plans_crud.create_plan(db, plan)
    db_plan_id = db_plan.id
    for place in plan.places:
        await places_crud.create_place(db, db_plan_id, place)
    return {"id": db_plan_id}


@router.get("/plans/{plan_id}")
async def list_plan(plan_id: int, db: AsyncSession = Depends(get_db)):
    return await plans_crud.get_task_by_id(db, plan_id)
