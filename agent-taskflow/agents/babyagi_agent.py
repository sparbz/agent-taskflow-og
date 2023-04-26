from . import Agent
from ..flows import BabyAGIExampleFlow

class BabyAGIAgent(Agent):
    def __init__(self, name="BabyAGIAgent", memory_backend=None):
        super().__init__(name, memory_backend)
        print(f"Hello, I am {name}. One moment as I load my avaialble flows.")
        babyagi_flow = BabyAGIExampleFlow(memory_backend=self.memory_backend)
        self.add_flow(babyagi_flow.name, babyagi_flow)

