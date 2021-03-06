import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskify.settings')

application = ProtocolTypeRouter({
    "ws": get_asgi_application(),
    "websocket": URLRouter([
        path('graphql-ws/', GraphqlSubscriptionConsumer)
    ]),
})
