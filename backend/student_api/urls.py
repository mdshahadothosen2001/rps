from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from .views.token import CustomTokenObtainPairView
from .views.semester import SemestersView, SemesterView


urlpatterns = [
    # POST: localhost:8000/user/token/
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="token"),
    # POST: localhost:8000/user/token/refresh/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GETT: localhost:8000/user/semester/
    path(route="semester/", view=SemestersView.as_view(), name="semester"),
    # GETT: localhost:8000/user/semester/
    path(route="semester/detail/", view=SemesterView.as_view(), name="semester_detail"),
]
