from .prompt_task import PromptTask

class ExecutionPromptTask(PromptTask):
    def __init__(self, name, objective, *args, **kwargs):
        self.name = name
        self.objective = objective
        # context = context_agent(query=objective, n=5)
        prompt = f"""
        You are an AI who performs one task based on the following objective: {objective}\n.
        Your task: {self.name}\nResponse:"""
        super().__init__(name=self.name, prompt=prompt, *args, **kwargs)

class TaskCreationPromptTask(PromptTask):
    def __init__(self, objective, result, task_description, task_list, *args, **kwargs):
        self.name = "Optimize a task creation list based on the result of an execution agent"
        self.objective = objective
        prompt = f"""
        You are a task creation AI that uses the result of an execution agent to create new tasks with the following objective: {objective},
        The last completed task has the result: {{result}}.
        This result was based on this task description: {task_description}. These are incomplete tasks: {', '.join(task_list)}.
        Based on the result, create new tasks to be completed by the AI system that do not overlap with incomplete tasks.
        Return the tasks as an array."""
        super().__init__(name=self.name, prompt=prompt, *args, **kwargs)

        # Schedule the prompt update to run before the task executes
        async def wrapped_update_prompt():
            await self.update_prompt(result)
        self.add_pre_execute_callback(wrapped_update_prompt)

    async def update_prompt(self, result):
        result_value = await result
        self.prompt = self.prompt.format(result=result_value)