# agent-taskflow

`agent-taskflow` is a task orchestration framework designed for AI Agents. It allows developers to create modular AI systems by defining agents, tasks, and flows for controlling the execution order of tasks. The framework aims to simplify the development and organization of AI agents by providing an intuitive and structured approach to managing tasks and task execution.

### Features

**Agents**: An Agent represents an AI agent and its ability to perform a set of refined tasks. Agents are responsible for the execution of individual tasks within a task flow.

**Tasks**: A Task is the atomic level of action for an Agent. It can be anything from a simple prompt with configurations to an API call or a Google search. Tasks can be easily extended and customized to fit various use cases.

**Flows**: A Flow is an ordered collection of tasks, allowing for complex execution patterns and control flow. Flows can contain cycles, making them more flexible than Directed Acyclic Graphs (DAGs).

### Installation

```
git clone
cd agent-taskflow
pip install -r requirements.txt
python -m agent-taskflow
```