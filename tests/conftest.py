import pytest

from src.user import User
from src.task import Task


@pytest.fixture
def first_user():
    return User(
        username='User',
        email='user@email.ru',
        first_name='User',
        last_name='Userov',
        task_list=[
            Task('Купить огурцы', 'Купить огурцы для салата'),
            Task('Купить помидоры', 'Купить помидоры для салата')
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username='User2',
        email='user2@email.ru',
        first_name='User2',
        last_name='Userov2',
        task_list=[
            Task('Купить огурцы', 'Купить огурцы для салата'),
            Task('Купить помидоры', 'Купить помидоры для салата'),
            Task('Купить лук', 'Купить дук для салата')
        ]
    )


@pytest.fixture
def task():
    return Task('Купить огурцы', 'Купить огурцы для салата', created_it='20.04.2024')
