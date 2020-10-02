from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.tasks.models import Tasks
from apps.tasks.serializers.tasks import TaskSerializer


class ReviewserializerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permisssion_class = [
        AllowAny,
    ]
