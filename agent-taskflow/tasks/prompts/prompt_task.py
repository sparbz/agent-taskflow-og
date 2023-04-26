import os
import openai
import pinecone
from .. import Task
from ...config.pinecone import init_pinecone

class PromptTask(Task):
    def __init__(self, name, prompt, config=None):
        self.prompt = prompt
        self.config = config or {}
        self.name = name
        self.lt = None
        self.pre_execute_callbacks = []

    def add_pre_execute_callback(self, callback):
        self.pre_execute_callbacks.append(callback)

    def get_ada_embedding(self, text):
        text = text.replace("\n", " ")
        return openai.Embedding.create(input=[text], model="text-embedding-ada-002")[
            "data"
        ][0]["embedding"]

    async def execute(self):
        print("\033[93m\033[1m" + "\nTask:" + "\033[0m\033[0m" + f" {self.name}")
        # Call all pre-execute callbacks
        for callback in self.pre_execute_callbacks:
            await callback()
        print(f"Prompt: {self.prompt}")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        try:
          messages = [{"role": "system", "content": self.prompt}]
          response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=messages,
              temperature=1.44,
              max_tokens=200,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0,
          )
          self.result = response.choices[0].message.content.strip()
          print(self.result)

        #   PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
        #   PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "")
        #   pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
        #   table_name = os.getenv("TABLE_NAME", "")
        #   index = pinecone.Index(table_name)

          table_name, index = init_pinecone()

          enriched_result = {
              "data": self.result
          }  # This is where you should enrich the result if needed
          result_id = f"result_{self.task['task_id']}"
          vector = self.get_ada_embedding(
              enriched_result["data"]
          )  # get vector of the actual result extracted from the dictionary
          index.upsert(
              [(result_id, vector, {"task": self.task["task_name"], "result": self.result})],
          namespace=self.objective
          )
          return self.result
        except openai.error.RateLimitError:
            print(
                "The OpenAI API rate limit has been exceeded. Waiting 10 seconds and trying again."
            )
