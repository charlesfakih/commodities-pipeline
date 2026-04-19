import time
import random
from app.core.processor import store_price, COMMODITIES

BASE_PRICES = {
    "WTI_OIL": 75.0,
    "COPPER": 3.80,
    "WHEAT": 5.50,
    "GOLD": 1950.0
}

def simulate_price(commodity: str) -> float:
    base = BASE_PRICES[commodity]
    change = random.uniform(-0.02, 0.02)
    return round(base * (1 + change), 2)

def run_simulator(interval: float = 1.0):
    print("Starting price simulator...")
    while True:
        for commodity in COMMODITIES:
            price = simulate_price(commodity)
            store_price(commodity, price)
            print(f"{commodity}: ${price}")
        time.sleep(interval)

if __name__ == "__main__":
    run_simulator()