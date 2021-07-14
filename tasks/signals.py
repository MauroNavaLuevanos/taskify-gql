from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription


from tasks.models import TaskModel

post_save.connect(post_save_subscription, sender=TaskModel)
# post_delete.connect(post_delete_subscription, sender=TaskModel, dispatch_uid='post_delete_task')

# @receiver(post_save, sender=TaskModel)
# def post_save_taks_handler(sender, **kwargs):
#     post_save_subscription(sender, **kwargs)
#     print('SIGNAL CALLED', sender)

