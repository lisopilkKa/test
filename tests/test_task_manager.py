import pytest
from ..src.task_manager import TaskManager 

def test_add_task():
    manager = TaskManager()
    manager.add_task("Написати код")
    assert "Написати код" in manager.list_tasks()

def test_remove_task():
    manager = TaskManager()
    manager.add_task("Тестувати програму")
    removed = manager.remove_task(0)
    assert removed == "Тестувати програму"
    assert len(manager.list_tasks()) == 0

def test_invalid_index():
    manager = TaskManager()
    with pytest.raises(IndexError):
        manager.remove_task(999)

def test_empty_task():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("   ")