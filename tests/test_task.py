def test_task_init(task):
    assert task.name == 'Купить огурцы'
    assert task.description == 'Купить огурцы для салата'
    assert task.status == 'Ожидает старта'
    assert task.created_it == '20.04.2024'
