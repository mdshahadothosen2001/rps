from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from .views.token import CustomTokenObtainPairView
from .views.semester import SemestersView, SemesterView
from .views.examination import ExaminationsView, ExaminationView
from .views.register import UserRegistrationView
from .views.answer import AnswerSubmittionView


urlpatterns = [
    # POST: localhost:8000/user/student-register/
    path(route="student-register/", view=UserRegistrationView.as_view(), name="register"),
    # POST: localhost:8000/user/token/
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="token"),
    # POST: localhost:8000/user/token/refresh/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GETT: localhost:8000/user/semester/
    path(route="semester/", view=SemestersView.as_view(), name="semester"),
    # GETT: localhost:8000/user/semester/
    path(route="semester/detail/", view=SemesterView.as_view(), name="semester_detail"),
    # GETT: localhost:8000/user/examination/
    path(route="examination/", view=ExaminationsView.as_view(), name="examination"),
    # GETT: localhost:8000/user/examination/
    path(route="examination/detail/", view=ExaminationView.as_view(), name="examination_detail"),
    # POST: localhost:8000/user/answer-submit/
    path(route="answer-submit/", view=AnswerSubmittionView.as_view(), name="answer_submit"),
]
