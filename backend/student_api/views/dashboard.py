from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from semester.models import Semester
from answer.models import Answer
from user.models import UserAccount
from utils.utils import tokenValidation


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        student_id = payload.get("id")
        students = UserAccount.objects.filter(is_student=True).count()
        semesters = Semester.objects.filter(students__id=student_id).count()
        answers = Answer.objects.filter(student__id=student_id).distinct().count()
        dashboard_data = {
            "total_student": students,
            "total_semesters": semesters,
            "total_examinations": answers,
            "due_semester": 8 - semesters
        }
        return Response(dashboard_data)
