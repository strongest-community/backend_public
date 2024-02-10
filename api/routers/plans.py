from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.plans as plans_crud
import api.schemas.plan as plan_schema
from api.db import get_db

router = APIRouter()


# ダミーデータ
plans = [
    {
        "id": 1,
        "description": "家族での休暇旅行計画",
        "budget": 300000,
        "situation": "家族旅行",
        "with_whom": "家族",
        "places": [
            {"id": 1, "plan_id": 1, "url": "https://example.com/place1"},
            {"id": 2, "plan_id": 1, "url": "https://example.com/place2"},
        ],
    },
    {
        "id": 2,
        "description": "友人との週末旅行",
        "budget": 50000,
        "situation": "友人との旅行",
        "with_whom": "友人",
        "places": [{"id": 3, "plan_id": 2, "url": "https://example.com/place3"}],
    },
]


@router.get("/plans/", response_model=List[plan_schema.Plan])
async def list_plans(db: AsyncSession = Depends(get_db)):
    """dami-deta function"""
    return await plans_crud.get_all_plans(db)


@router.post("/plans/")
async def create_plan(plan: plan_schema.PlanCreate, db: AsyncSession = Depends(get_db)):
    return await plans_crud.create_plan(db=db, plan=plan)


# @router.get("/plans/{plan_id}")
# async def list_plans(plan_id: int):
#     for plan in plans:
#         if plan["id"] == plan_id:
#             return plan
