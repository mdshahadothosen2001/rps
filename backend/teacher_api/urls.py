from django.urls import path

from .views.answer import AnswerListView
from .views.semester_done import SemesterDoneView, SemestersView
from .views.examination import ExaminationCreateView
from .views.result import MarkEachCourseView, GPACalculateView


urlpatterns = [
    # GET: localhost:8000/user/answer-list/
    path(route="answer-list/", view=AnswerListView.as_view(), name="answer_list"),
    # GET: localhost:8000/user/semester-list-for-teacher/
    path(route="semester-list-for-teacher/", view=SemestersView.as_view(), name="semester_list"),
    # PATCH: localhost:8000/user/semester-done/
    path(route="semester-done/", view=SemesterDoneView.as_view(), name="semester_done"),
    # POST: localhost:8000/user/add-examination/
    path(route="add-examination/", view=ExaminationCreateView.as_view(), name="examination_create"),
    # POST: localhost:8000/user/add-result-each-course/
    path(route="add-result-each-course/", view=MarkEachCourseView.as_view(), name="mark_add"),
    # POST: localhost:8000/user/semester-result-add-result/
    path(route="semester-result-add-result/", view=GPACalculateView.as_view(), name="semester_result_add"),
]
