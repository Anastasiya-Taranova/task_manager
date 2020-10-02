from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from apps.tasks.apps import TasksConfig
from apps.tasks.views.tasks import Review

app_name = TasksConfig.label

router = DefaultRouter()
router.register("tasks", Review, "tasks")

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
    path("", include(router.urls)),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
