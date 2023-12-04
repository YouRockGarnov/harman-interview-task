from dataclasses import dataclass


@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int


@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str


class TaskQueue:
    def __init__(self):
        self.priority_queues = {}

    def add_task(self, task: Task):
        if task.priority not in self.priority_queues:
            self.priority_queues[task.priority] = []
        self.priority_queues[task.priority].append(task)

    def get_task(self, available_resources: Resources) -> Task:
        for priority in sorted(self.priority_queues.keys(), reverse=True):
            for i in range(len(self.priority_queues[priority])):
                task = self.priority_queues[priority][i]
                if self.can_process(task.resources, available_resources):
                    del self.priority_queues[priority][i]
                    return task
        return None

    def can_process(self, required_resources: Resources, available_resources: Resources) -> bool:
        return (
            available_resources.ram >= required_resources.ram
            and available_resources.cpu_cores >= required_resources.cpu_cores
            and available_resources.gpu_count >= required_resources.gpu_count
        )
