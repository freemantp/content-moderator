from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from models import (
    CategoryDescription,
    OffensivenessCategoryPrediction,
    ClassificationRequest,
)
from moderation_service import ModerationService

services = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    services["moderation"] = ModerationService()
    yield


def get_moderation_service() -> ModerationService:
    return services["moderation"]


app = FastAPI(title='Text moderation service', lifespan=lifespan)


def show_docs():
    return RedirectResponse("/docs")

@app.get("/labels")
def get_label_descriptions(
    mod_service: ModerationService = Depends(get_moderation_service),
) -> CategoryDescription:
    return mod_service.get_category_descriptions()


@app.post("/classify")
async def classify_text(
    body: ClassificationRequest,
    mod_service: ModerationService = Depends(get_moderation_service),
) -> OffensivenessCategoryPrediction:
    return mod_service.classify_text(input_text=body.text)
