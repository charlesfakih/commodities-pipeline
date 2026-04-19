import json
import time
from app.core.redis_client import get_redis_client

COMMODITIES = ["WTI_OIL", "COPPER", "WHEAT", "GOLD"]
MAX_HISTORY = 100

def store_price(commodity: str, price: float):
    client = get_redis_client()
    record = json.dumps({
        "commodity": commodity,
        "price": price,
        "timestamp": time.time()
    })
    client.lpush(f"prices:{commodity}", record)
    client.ltrim(f"prices:{commodity}", 0, MAX_HISTORY - 1)

def get_latest_price(commodity: str) -> dict | None:
    client = get_redis_client()
    record = client.lindex(f"prices:{commodity}", 0)
    return json.loads(record) if record else None # type: ignore

def get_stats(commodity: str) -> dict | None:
    client = get_redis_client()
    records: list = client.lrange(f"prices:{commodity}", 0, -1) # type: ignore
    if not records:
        return None
    prices = [json.loads(r)["price"] for r in records]
    return {
        "commodity": commodity,
        "latest_price": prices[0],
        "average": sum(prices) / len(prices),
        "min_price": min(prices),
        "max_price": max(prices),
        "sample_count": len(prices)
    }

def get_moving_average(commodity: str, window: int = 10) -> float | None:
    client = get_redis_client()
    records: list = client.lrange(f"prices:{commodity}", 0, window - 1) # type: ignore
    if not records:
        return None
    prices = [json.loads(r)["price"] for r in records]
    return sum(prices) / len(prices)
