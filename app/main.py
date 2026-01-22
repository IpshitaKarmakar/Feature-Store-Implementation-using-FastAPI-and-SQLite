from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd

from .database import Base, engine, SessionLocal
from .models import RawData, Feature
from .schemas import RawDataIn
from .feature_engineering import compute_features

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Feature Store (Python 3.9)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register_raw")
def register_raw(data: RawDataIn, db: Session = Depends(get_db)):
    record = RawData(entity_id=data.entity_id, value=data.value)
    db.add(record)
    db.commit()
    return {"message": "Raw data registered"}

@app.post("/compute_features/{entity_id}")
def compute_and_store(entity_id: str, db: Session = Depends(get_db)):
    rows = db.query(RawData).filter(RawData.entity_id == entity_id).all()
    if not rows:
        raise HTTPException(status_code=404, detail="No raw data found")

    df = pd.DataFrame([{"value": r.value} for r in rows])
    features = compute_features(df)

    version = db.query(Feature).filter(Feature.entity_id == entity_id).count() + 1
    for name, value in features.items():
        f = Feature(entity_id=entity_id, feature_name=name, feature_value=value, version=version)
        db.add(f)
    db.commit()
    return {"message": "Features computed", "version": version}

@app.get("/get_features/{entity_id}")
def get_features(entity_id: str, db: Session = Depends(get_db)):
    features = db.query(Feature).filter(Feature.entity_id == entity_id).all()
    if not features:
        raise HTTPException(status_code=404, detail="No features found")
    return features
