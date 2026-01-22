from pydantic import BaseModel

class RawDataIn(BaseModel):
    entity_id: str
    value: float
