from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.tasks.models import Tasks
from apps.tasks.permissions import IsOrganizerOrReadOnly
from apps.tasks.serializers.tasks import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        AllowAny,
    ]
