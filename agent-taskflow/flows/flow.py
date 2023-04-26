import asyncio

class Flow:
    def __init__(self, name, memory_backend):
        self.tasks = []
        self.name = name
        self.task_id = 0  # Initialize the task_id counter
        self.memory_backend = memory_backend
        # Print TASKFLOW
        print("\033[93m\033[1m" + f"\n*****TASKFLOW \033[91m\033[1m {self.name} \033[93m\033[1m LOADED*****\n" + "\033[0m\033[0m")

    async def add_task(self, task, order=None):
        task.task_id = self.task_id  # Assign the current task_id to the new task
        self.task_id += 1  # Increment the task_id counter

        task.task = {
            "task_id": task.task_id,
            "task_name": task.name
        }
        if order is None:
            self.tasks.append(task)
        else:
            self.tasks.insert(order, task)

    async def remove_task(self, task):
        self.tasks.remove(task)

    async def run_task(self, task, *args, **kwargs):
        if task in self.tasks:
            await task.execute(*args, **kwargs)
            await self.remove_task(task)

    async def run(self, *args, **kwargs):
        while self.tasks:
            task = self.tasks[0]
            await task.execute(*args, **kwargs)
            await self.remove_task(task)
