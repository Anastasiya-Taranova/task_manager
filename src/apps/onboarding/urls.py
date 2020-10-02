from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.onboarding.apps import OnboardingConfig
from apps.onboarding.views.user import UserList

app_name = OnboardingConfig.label

router = DefaultRouter()
router.register("user", UserList, "users")

urlpatterns = [
    path("", include(router.urls)),
]
