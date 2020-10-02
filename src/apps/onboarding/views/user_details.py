from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.onboarding.serializers.user import UserSerializer

User = get_user_model()


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]
