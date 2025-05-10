class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        """Додає завдання до списку."""
        if not task.strip():
            raise ValueError("Завдання не може бути порожнім!")
        self.tasks.append(task)

    def remove_task(self, task_index: int) -> str:
        """Видаляє завдання за індексом."""
        if task_index < 0 or task_index >= len(self.tasks):
            raise IndexError("Невірний індекс завдання!")
        return self.tasks.pop(task_index)

    def list_tasks(self) -> list:
        """Повертає список усіх завдань."""
        return self.tasks.copy()

    def clear_all(self) -> None:
        """Очищає список завдань."""
        self.tasks.clear()