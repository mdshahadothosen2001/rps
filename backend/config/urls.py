from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="user/",
        view=include("student_api.urls"),
        name="user",
    ),
    path(
        route="user/",
        view=include("teacher_api.urls"),
        name="user",
    ),
]
