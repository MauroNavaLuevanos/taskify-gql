import graphene
from graphene_django import DjangoObjectType

from tasks.models import TaskModel


class TaskType(DjangoObjectType):
    class Meta:
        model = TaskModel
        fields = ('name', 'created', 'complete', 'id',)
