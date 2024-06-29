from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from semester.models import Semester
from utils.utils import tokenValidation
from ..serializers.students import StudentListSerializer


class StudentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        teacher_id = payload.get("id")
        students = get_list_or_404(Semester, teachers__id=teacher_id)
        serializers = StudentListSerializer(students, many=True)
        return Response(serializers.data)
