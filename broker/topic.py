import asyncio
from typing import List

class Topic:
    def __init__(self, name: str):
        self.name = name
        self.subscribers: List[asyncio.Queue] = []

    async def publish(self, message: dict):
        for subscriber in self.subscribers:
            await subscriber.put(message)

    def add_subscriber(self) -> asyncio.Queue:
        queue = asyncio.Queue()
        self.subscribers.append(queue)
        return queue