from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.tasks.models import Tasks
from apps.tasks.serializers.tasks import TaskSerializer


class Review(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "finished_day"]

    def get_queryset(self):
        author_id = -1
        if not self.request.user.is_anonymous:
            author_id = self.request.user.pk

        qs = Tasks.objects.filter(author_id=author_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
