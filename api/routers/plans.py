from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/plans/")
async def list_plans():
    """dami-deta function"""
    return {"plans": plans}

@router.post("/plans/")
async def create_plan(plan: schemas.PlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db=db, plan=plan)

@router.get("/plans/{plan_id}")
async def list_plans(plan_id: int):
    for plan in plans:
        if plan["id"] == plan_id:
            return plan