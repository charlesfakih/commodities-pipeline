from broker.broker import Broker

class Producer:
    def __init__(self, broker: Broker, topic_name: str):
        self.broker = broker
        self.topic_name = topic_name

    async def send(self, message: dict):
        await self.broker.publish(self.topic_name, message)