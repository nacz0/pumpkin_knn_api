from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from app import model

app = FastAPI(title="Pumpkin Seeds k-NN Classifier")

class SampleInput(BaseModel):
    features: List[float]
    method: str = Query("soft", enum=["soft", "hard"])
    k: int = 3

@app.post("/predict")
def classify(sample: SampleInput):
    if len(sample.features) != 12:
        return {"error": "Dokladnie 12 cech wymagane"}
    prediction = model.predict_knn(sample.features, sample.method, sample.k)
    return {"predicted_class": prediction}
