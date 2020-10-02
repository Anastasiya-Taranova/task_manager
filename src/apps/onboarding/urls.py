from django.urls import path

from apps.onboarding.apps import OnboardingConfig
from apps.onboarding.views.user_details import UserDetail
from apps.onboarding.views.user_list import UserList

app_name = OnboardingConfig.label

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
]
