from . import Task

class GoogleSearchTask(Task):
    def __init__(self, query, config=None):
        self.query = query
        self.config = config or {}

    def execute(self, agent):
        # Pass the task's query and config to the agent
        return agent.perform_task(self)
