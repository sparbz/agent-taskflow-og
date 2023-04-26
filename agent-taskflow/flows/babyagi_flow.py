from . import Flow
from ..tasks import TaskCreationPromptTask, ExecutionPromptTask

import asyncio

class BabyAGIExampleFlow(Flow):
    def __init__(self, memory_backend):
        super().__init__(name="BabyAGIExampleFlow", memory_backend=memory_backend)
        self.execution_result_future = asyncio.Future() 

    async def init_tasks(self):
        self.objective = input("Enter the objective: ")
        self.initial_task = "Develop a task list based on the objective"

        self.execution_prompt_task = ExecutionPromptTask(
            name=self.initial_task,
            objective=self.objective,)
        await self.add_task(self.execution_prompt_task)

        self.task_creation_prompt_task = TaskCreationPromptTask(
            objective=self.objective,
            result=self.execution_result_future,  # Use the Future object as the result
            task_description=self.execution_prompt_task.objective,
            task_list=[t.task['task_name'] for t in self.tasks])
        await self.add_task(self.task_creation_prompt_task)

    async def run(self, *args, **kwargs):
        await self.init_tasks()
        while self.tasks:
            print([t.name for t in self.tasks])
            task = self.tasks[0]
            result = await task.execute(*args, **kwargs)
            if task is self.execution_prompt_task:
                self.execution_result_future.set_result(result)  # Use asyncio.Future.set_result()
            elif task is self.task_creation_prompt_task:
                for t in result.split("\n"):
                    await self.add_task(ExecutionPromptTask(
                        objective=self.objective,
                        name=t,
                    ))
            await self.remove_task(task)
