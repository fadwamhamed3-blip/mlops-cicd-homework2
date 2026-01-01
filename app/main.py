from fastapi import FastAPI
from pydantic import BaseModel

from app.feature_engineering import hashed_feature
from app.model import DummyModel

app = FastAPI(title="High-Cardinality Prediction Service")

model = DummyModel()

class PredictRequest(BaseModel):
    user_id: str
    num_buckets: int = 1000


@app.get("/health")
def health():


    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):

    
    bucket = hashed_feature(req.user_id, req.num_buckets)
    pred = model.predict(bucket)
    return {"bucket": bucket, "prediction": pred}
