from django.contrib.auth import get_user_model
from django.db import models

from apps.tasks.consts import ReminderStatus

User = get_user_model()


class Tasks(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=250)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=200,
        choices=ReminderStatus.to_choices(),
        default=ReminderStatus.CREATED.name,
        db_index=True,
    )
    finished_day = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"pk={self.pk},"
            f"name={self.name},"
            f"description={self.description},"
            f" status={self.status},"
            f" creation_date={self.creation_date},"
            f")"
        )
