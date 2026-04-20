from broker.topic import Topic

class Broker:
    def __init__(self):
        self.topics: dict[str, Topic] = {}

    def create_topic(self, name: str) -> Topic:
        if name not in self.topics:
            self.topics[name] = Topic(name)
        return self.topics[name]
    
    def get_topic(self, name: str) -> Topic | None:
        return self.topics.get(name)
    
    async def publish(self, topic_name: str, message: dict):
        topic = self.get_topic(topic_name)
        if topic is None:
            topic = self.create_topic(topic_name)
        await topic.publish(message)