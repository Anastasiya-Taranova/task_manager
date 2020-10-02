from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("apps.onboarding.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
