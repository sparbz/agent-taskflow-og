from . import Task

class APICallTask(Task):
    def __init__(self, api_call, config=None):
        self.api_call = api_call
        self.config = config or {}

    def execute(self, agent):
        # Pass the task's API call and config to the agent
        return agent.perform_task(self)
