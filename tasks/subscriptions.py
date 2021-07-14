import graphene
from graphene_subscriptions.events import CREATED

from tasks.types import TaskType

from tasks.models import TaskModel as Task


class TaskSubscription(graphene.ObjectType):
    task_created = graphene.Field(TaskType)

    def resolve_task_created(root, info):

        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Task)
        ).map(lambda event: event.instance)