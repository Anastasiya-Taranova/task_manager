from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, reverse_lazy


def index(r):
    return HttpResponse(
        f"""
        <a href="{reverse_lazy('tasks:tasks-list')}">Users API</a>
        <a href="{reverse_lazy('tasks:tasks-list')}">Tasks API</a>
        """
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", index),
    path("api/o/", include("apps.onboarding.urls")),
    path("api/t/", include("apps.tasks.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
