from datetime import datetime

from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import UserAccount
from gpa.models import GPA
from mark.models import Mark
from ..serializers.result import SemesterResultSerializer, MarkEachCourseSerializer
from utils.utils import tokenValidation


class SemesterResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        student_id = payload.get("id")
        semester_id = request.query_params.get("semester_id")
        student_data = get_object_or_404(UserAccount, id=student_id)
        result = get_object_or_404(GPA, student__id=student_id, semester__id=semester_id)
        marks = get_list_or_404(Mark, examination__semester__id=semester_id, examination__name="final")
        marks_serializer = MarkEachCourseSerializer(marks, many=True)
        serializer = SemesterResultSerializer(result)
        result = {
            "first_name": student_data.first_name,
            "last_name": student_data.last_name,
            "registration": student_data.username,
            "roll": student_data.roll,
            "GPA": serializer.data.get("point"),            
            "course_wise": marks_serializer.data,
            "date": datetime.now().date()
        }
        return Response(result)


class SemesterFinalResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        student_id = payload.get("id")
        student_data = get_object_or_404(UserAccount, id=student_id)
        result = GPA.objects.filter(student__id=student_id)
        total_point = result.aggregate(total_point=Sum("point"))["total_point"]
        total_passed_semester = result.aggregate(total_passed_semester=Count("id"))["total_passed_semester"]
        serializer = SemesterResultSerializer(result, many=True)
        if total_passed_semester == 8:
            result = {
                "first_name": student_data.first_name,
                "last_name": student_data.last_name,
                "registration": student_data.username,
                "roll": student_data.roll,
                "CGPA": total_point,            
                "semester_wise": serializer.data,
                "date": datetime.now().date()
            }
            return Response(result)
        
        return Response("not found")
