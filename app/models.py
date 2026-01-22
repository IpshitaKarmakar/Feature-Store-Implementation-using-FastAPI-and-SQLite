from sqlalchemy import Column, Integer, String, Float
from .database import Base

class RawData(Base):
    __tablename__ = "raw_data"
    id = Column(Integer, primary_key=True, index=True)
    entity_id = Column(String, index=True)
    value = Column(Float)

class Feature(Base):
    __tablename__ = "features"
    id = Column(Integer, primary_key=True, index=True)
    entity_id = Column(String, index=True)
    feature_name = Column(String)
    feature_value = Column(Float)
    version = Column(Integer)
