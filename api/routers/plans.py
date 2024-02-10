from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import api.cruds.plans as plan_crud
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
            {
                "id": 1,
                "plan_id": 1,
                "url": "https://example.com/place1"
            },
            {
                "id": 2,
                "plan_id": 1,
                "url": "https://example.com/place2"
            }
        ]
    },
    {
        "id": 2,
        "description": "友人との週末旅行",
        "budget": 50000,
        "situation": "友人との旅行",
        "with_whom": "友人",
        "places": [
            {
                "id": 3,
                "plan_id": 2,
                "url": "https://example.com/place3"
            }
        ]
    }
]



@router.get("/plans/")
async def list_plans():
    """dami-deta function"""
    return {"plans": plans}

@router.post("/plans/", response_model=plan_schema.PlanCreateResponse)
async def create_plan(plan: plan_schema.PlanCreate, db: Session = Depends(get_db)):
    db_plan = await plan_crud.create_plan(db=db, plan=plan)

    return db_plan

@router.get("/plans/{plan_id}")
async def list_plans(plan_id: int):
    for plan in plans:
        if plan["id"] == plan_id:
            return plan