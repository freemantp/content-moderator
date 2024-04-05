from pydantic import BaseModel, PositiveFloat

class OffensivenessCategoryPrediction(BaseModel): 
    predictions: dict[str, PositiveFloat]

class CategoryDescription(BaseModel): 
    descriptions: dict[str, str]     

class ClassificationRequest(BaseModel):
    text: str