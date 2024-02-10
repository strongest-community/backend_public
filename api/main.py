"""main module"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import sample, plans

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the sample router
app.include_router(sample.router)
app.include_router(plans.router)
