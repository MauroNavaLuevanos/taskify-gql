from django.db import models


class TaskModel(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    complete = models.BooleanField(_("Complete"), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
