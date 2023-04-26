class Task:
    def __init__(self, config=None):
        self.task_id = None

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Tasks must implement the execute method")
