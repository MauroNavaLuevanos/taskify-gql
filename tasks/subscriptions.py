import graphene
from graphene_subscriptions.events import CREATED, UPDATED, DELETED

from tasks.types import TaskType

from tasks.models import TaskModel as Task


class TaskSubscription(graphene.ObjectType):
    task_created = graphene.Field(TaskType)


    def resolve_task_created(root, info):
        METHODS = [
            CREATED,
            UPDATED,
            DELETED
        ]

        return root.filter(
            lambda event:
                event.operation in METHODS and
                isinstance(event.instance, Task)
        ).map(lambda event: event.instance)