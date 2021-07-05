import graphene

from GraphQL.types import TaskType

from tasks.models import TaskModel


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, name):
        task = TaskModel.objects.create(name=name)
        task.save()

        return CreateTaskMutation(task=task)

class DeleteTaskMutation(graphene.Mutation):
    class Arguments:
        taskId = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, taskId):
        task = TaskModel.objects.get(id=taskId)
        task.delete()

        return DeleteTaskMutation(ok=True)


class UpdateTaskMutation(graphene.Mutation):
    class Arguments:
        taskId = graphene.ID(required=True)
        name = graphene.String(required=False)
        complete = graphene.Boolean(required=False)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, name=None, taskId=None, complete=None):
        task = TaskModel.objects.get(id=taskId)

        if name:
            task.name = name

        if complete != None:
            task.complete = complete

        task.save()

        return UpdateTaskMutation(task=task)


class Mutation(graphene.ObjectType):
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()
    delete_task = DeleteTaskMutation.Field()
