"""main module"""

from fastapi import FastAPI

from api.routers import sample

app = FastAPI()

# Include the sample router
app.include_router(sample.router)
