from pydantic import BaseModel

class PriceRecord(BaseModel):
    commodity: str
    price: float
    timestamp: float

class StatsResponse(BaseModel):
    commodity: str
    latest_price: float
    average: float
    min_price: float
    max_price: float
    sample_count: int