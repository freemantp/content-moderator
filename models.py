from pydantic import BaseModel, PositiveFloat

class CategoryPrediction(BaseModel): 
    predictions: dict[str, PositiveFloat] 

class ClassificationRequest(BaseModel):
    text: str