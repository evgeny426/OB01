# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.
from typing import List, Any


class Task:
    def __init__(self, description_task, period_execution):
        self.description_task = description_task
        self.period_execution = period_execution
        self.status = False

    def mark_completed(self):
        self.status = True


class TaskManager:
    def __init__(self):
        self.list_tasks = []

    def add_task(self, description_task, period_execution):
        task = Task(description_task, period_execution)
        self.list_tasks.append(task)
        return task

    def mark_task_completed(self, task):
        if task in self.list_tasks:
            task.mark_completed()

    def list_current_tasks(self):
        current_tasks = []
        for task in self.list_tasks:
            if not task.status:
                current_tasks.append(task)
        if not current_tasks:
            print("Все задачи выполнены!")
        else:
            for task in current_tasks:
                if task.status:
                    completed_status = 'Выполнено'
                else:
                    completed_status = 'Не выполнено'
                print(f"{task.description_task} (Срок выполнения: {task.period_execution}) - {completed_status}")



task_manager = TaskManager()

task1 = task_manager.add_task("Сходить в магазин.", "3")
task2 = task_manager.add_task("Написать программу.", "4")

print("Текущие (не выполненные) задачи:")
task_manager.list_current_tasks()

task_manager.mark_task_completed(task1)

print("\nТекущие (не выполненные) задачи:")
task_manager.list_current_tasks()


