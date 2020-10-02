from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from apps.tasks.apps import TasksConfig
from apps.tasks.views.all_tasks import TaskList
from apps.tasks.views.review_detail import ReviewserializerDetailView

app_name = TasksConfig.label

schema_view = get_schema_view(
    openapi.Info(
        title="Users API",
        default_version="v1",
        description="The API is the API",
        terms_of_service="TBD",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("all/", TaskList.as_view()),
    path("<int:pk>/edit", ReviewserializerDetailView.as_view(), name="review-details"),
]
