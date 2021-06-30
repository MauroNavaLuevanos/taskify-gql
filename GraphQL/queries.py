import graphene

from tasks.models import TaskModel

from GraphQL.types import TaskType


class Query(graphene.ObjectType):

    tasks =  graphene.List(TaskType)
    task =  graphene.Field(TaskType, taskId=graphene.ID(required=True))

    def resolve_tasks(root, info):
        return TaskModel.objects.all()

    def resolve_task(root, info, taskId):
        return TaskModel.objects.get(id=taskId)
