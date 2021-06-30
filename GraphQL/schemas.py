from graphene import Schema

from GraphQL.queries import Query
from GraphQL.mutations import Mutation


schema = Schema(query=Query, mutation=Mutation)