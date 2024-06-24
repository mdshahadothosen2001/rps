from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from semester.models import Semester
from ..serializers.semester import SemestersSerializer
from utils.utils import tokenValidation


class SemestersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        student_id = payload.get("id")
        semesters = Semester.objects.filter(students__id=student_id)
        serializers = SemestersSerializer(semesters, many=True)
        return Response(serializers.data)
