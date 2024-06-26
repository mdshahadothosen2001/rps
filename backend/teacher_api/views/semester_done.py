from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from semester.models import Semester

class SemesterDoneView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        semester_id = request.data.get("semester_id")
        
        semester = get_object_or_404(Semester, id=semester_id)
        semester.is_active = False
        semester.save()
        return Response("success")
