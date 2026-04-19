from fastapi import FastAPI, HTTPException
from app.core.processor import get_latest_price, get_stats, get_moving_average, COMMODITIES

app = FastAPI(title="Commodities Pipeline API")

@app.get("/price/{commodity}")
def get_price(commodity: str):
    commodity = commodity.upper()
    if commodity not in COMMODITIES:
        raise HTTPException(status_code=404, detail=f"{commodity} not found")
    result = get_latest_price(commodity)
    if not result:
        raise HTTPException(status_code=404, detail="No data yet")
    return result

@app.get("/average/{commodity}")
def get_average(commodity: str, window: int = 10):
    commodity = commodity.upper()
    if commodity not in COMMODITIES:
        raise HTTPException(status_code=404, detail=f"{commodity} not found")
    average = get_moving_average(commodity, window=window)
    if average is None:
        raise HTTPException(status_code=404, detail="No data yet")
    return {"commodity": commodity, "moving_average": average, "window": window}

@app.get("/stats/{commodity}")
def get_stats_route(commodity: str):
    commodity = commodity.upper()
    if commodity not in COMMODITIES:
        raise HTTPException(status_code=404, detail=f"{commodity} not found")
    stats = get_stats(commodity)
    if not stats:
        raise HTTPException(status_code=404, detail="No data yet")
    return stats