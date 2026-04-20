import asyncio
import time
import random
from broker.broker import Broker
from broker.producer import Producer
from broker.consumer import Consumer
from app.core.processor import store_price

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

async def price_handler(message:dict):
    store_price(message["commodity"], message["price"])
    print(f"{message['commodity']}: ${message['price']}")

async def run_pipeline():
    broker = Broker()
    broker.create_topic("prices")

    producer = Producer(broker, "prices")
    consumer = Consumer(broker, "prices", price_handler)

    consumer.subscribe()

    async def produce():
        while True:
            for commodity in BASE_PRICES:
                price = simulate_price(commodity)
                await producer.send({
                    "commodity": commodity,
                    "price": price,
                    "timestamp": time.time()
                })
            await asyncio.sleep(1)

    await asyncio.gather(produce(), consumer.start())

if __name__ == "__main__":
    asyncio.run(run_pipeline())