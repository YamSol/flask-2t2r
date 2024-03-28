import typing
import strawberry
from database_connect import connect

@strawberry.type
class Task:
    name: str
    checked: bool
    id: int

# def get_tasks() -> typing.List[Task]:
#     # Assuming 'connect' returns an instance of your database client
#     client = connect(db_type='postgres', database='todo_list', table='tasks')
#     tasks_from_db = client.get_all()
#     tasks = []
#     for task_data in tasks_from_db:
#         task = Task(name=task_data['name'], checked=task_data['checked'], id=task_data['id'])
#         tasks.append(task)  
#     return tasks

def get_tasks() -> typing.List[Task]:
    # Assuming 'connect' returns an instance of your database client
    client = connect(db_type='postgres', database='todo_list', table='tasks')
    tasks = client.get_all()  # Assuming this returns a list of tuples
    return [Task(name=t['name'], checked=t['checked'], id=t['id']) for t in tasks]


@strawberry.type
class Query:
    tasks: typing.List[Task] = strawberry.field(resolver=get_tasks)

# @strawberry.type
# class Query:
#     @strawberry.field
#     def tasks(self) -> typing.List[Task]:
#         client = connect(db_type='postgres', database='todo_list', table='tasks')
#         tasks_from_db = client.get_all()  # Assuming this returns a list of tuples]
#         print(tasks_from_db[0])
#         tasks = [Task(*task_data) for task_data in tasks_from_db]  # Create Task objects
#         return tasks

schema = strawberry.Schema(query=Query)