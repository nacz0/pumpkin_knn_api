from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from app import model

app = FastAPI(title="Pumpkin Seeds k-NN Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class SampleInput(BaseModel):
    features: List[float]
    method: str = Query("soft", enum=["soft", "hard"])
    k: int = 3

@app.post("/predict")
def classify(sample: SampleInput):
    if len(sample.features) != 12:
        return {"error": "Wymagane jest dokładnie 12 cech"}
    prediction = model.predict_knn(sample.features, sample.method, sample.k)
    return {"predicted_class": prediction}