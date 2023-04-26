class Agent:
    def __init__(self, name, memory_backend):
        self.flows = {}
        self.name = name
        self.memory_backend = memory_backend
        print("\033[94m\033[1m" + "\n*****AGENT LOADED*****\n" + "\033[0m\033[0m")
        print(f"{self.name}")

    def add_flow(self, name, taskflow):
        self.flows[name] = taskflow

    def remove_flow(self, name):
        if name in self.flows:
            del self.flows[name]

    def get_flow_names(self):
        return list(self.flows.keys())

    def select_flow(self, name):
        return self.flows.get(name)

    async def execute(self, flow, *args, **kwargs):
        await flow.run(*args, **kwargs)

    async def run(self):
        flow_names = self.get_flow_names()
        if not flow_names:
            print("No flows available")
            return
        print("Available flows:")
        for i, name in enumerate(flow_names, start=1):
            print(f"{i}. {name}")
        selection = input("Enter flow number to run: ")
        try:
            selection_index = int(selection) - 1
            if selection_index < 0 or selection_index >= len(flow_names):
                raise ValueError
            selected_flow_name = flow_names[selection_index]
            selected_flow = self.select_flow(selected_flow_name)
            await self.execute(selected_flow)
        except ValueError:
            print("Invalid selection")
