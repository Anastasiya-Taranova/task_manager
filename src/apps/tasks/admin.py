from django.contrib import admin

from apps.tasks.models import Tasks


@admin.register(Tasks)
class TasksAdminModel(admin.ModelAdmin):
    pass
