import asyncio
from broker.broker import Broker
from typing import Callable

class Consumer:
    def __init__(self, broker: Broker, topic_name: str, handler: Callable):
        self.broker = broker
        self.topic_name = topic_name
        self.handler = handler
        self.queue: asyncio.Queue | None = None

    def subscribe(self):
        topic = self.broker.get_topic(name=self.topic_name)
        if topic is None:
            topic = self.broker.create_topic(self.topic_name)
        self.queue = topic.add_subscriber()

    async def start(self):
        self.subscribe()
        while True:
            message = await self.queue.get() # type: ignore
            await self.handler(message)