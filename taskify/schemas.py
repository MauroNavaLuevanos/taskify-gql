import graphene

from tasks.queries import Query as TaskQuery

from tasks.mutations import Mutation as TaskMutation

from tasks.subscriptions import TaskSubscription


class Query(TaskQuery, graphene.ObjectType):
    pass

class Mutation(TaskMutation, graphene.ObjectType):
    pass

class Subscription(TaskSubscription):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)
