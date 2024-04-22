import datetime


class Task:
    name: str
    description: str
    status: str
    created_it: str

    def __init__(self, name, description, status='Ожидает старта', created_it=None):
        self.name = name
        self.description = description
        self.status = status
        self.created_it = created_it if created_it else datetime.date.today().strftime('%d.%m.%Y')


if __name__ == '__main__':
    task = Task('Купить огурцы', 'Купить огурцы для салата')

    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_it)
