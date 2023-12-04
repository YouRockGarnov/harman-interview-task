import pytest
from task_queue import Task, Resources, TaskQueue


@pytest.fixture
def task_queue():
    return TaskQueue()


def test_task_queue(task_queue):
    task1 = Task(id=1, priority=1, resources=Resources(ram=16, cpu_cores=16, gpu_count=16), content="Task 1", result="")
    task2 = Task(id=2, priority=2, resources=Resources(ram=8, cpu_cores=2, gpu_count=2), content="Task 2", result="")
    task3 = Task(id=3, priority=1, resources=Resources(ram=1, cpu_cores=1, gpu_count=1), content="Task 3", result="")
    task_queue.add_task(task1)
    task_queue.add_task(task2)
    task_queue.add_task(task3)
    
    consumed_task = task_queue.get_task(Resources(0, 0, 0))
    assert consumed_task is None
    
    consumed_task = task_queue.get_task(Resources(1, 1, 1))
    assert consumed_task.id == 3
    
    consumed_task = task_queue.get_task(Resources(8, 2, 2))
    assert consumed_task.id == 2
    
    consumed_task = task_queue.get_task(Resources(16, 16, 16))
    assert consumed_task.id == 1
    
    
