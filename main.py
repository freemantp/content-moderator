from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI, Depends
from fastapi.responses import RedirectResponse
from prometheus_fastapi_instrumentator import Instrumentator

from models import (
    CategoryDescription,
    OffensivenessCategoryPrediction,
    ClassificationRequest,
)
from moderation_service import ModerationService
from rps_tracking import RPSMiddleware

services = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    services["moderation"] = ModerationService()
    yield

def get_moderation_service() -> ModerationService:
    return services["moderation"]

app = FastAPI(title="Content moderation service", lifespan=lifespan)

# Add prometheous instumentation and register the rps tracking middlewae
Instrumentator().instrument(app).expose(app)
app.add_middleware(RPSMiddleware)

v1_api = APIRouter(prefix="/api/v1")

@app.get("/", include_in_schema=False)
async def show_docs():
    return RedirectResponse("/docs")

@v1_api.post("/classify")
async def classify_text(body: ClassificationRequest, mod_service: ModerationService = Depends(get_moderation_service)) -> OffensivenessCategoryPrediction:
    return mod_service.classify(input_text=body.text)

@v1_api.get("/labels")
async def get_label_descriptions(mod_service: ModerationService = Depends(get_moderation_service)) -> CategoryDescription:
    return mod_service.get_category_descriptions()

app.include_router(v1_api)