from contextlib import asynccontextmanager
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from models import CategoryPrediction, ClassificationRequest
from moderation_service import ModerationService

services = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    services['moderation'] = moderation_service = ModerationService()
    yield

    # Clean up resources before shutdown
    services['moderation'].cleanup()

def get_moderation_service() -> ModerationService:
    return services['moderation']

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root(mod_service: ModerationService = Depends(get_moderation_service)):
    return RedirectResponse("/docs")

@app.post("/classify")
async def create_item(body: ClassificationRequest, mod_service: ModerationService = Depends(get_moderation_service)) -> CategoryPrediction:
    return mod_service.classify_text(input_text=body.text)
