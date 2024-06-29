from datetime import datetime

from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from user.models import UserAccount
from gpa.models import GPA
from semester.models import Semester
from mark.models import Mark
from ..serializers.result import SemesterResultSerializer, MarkEachCourseSerializer, SemesterResultCreateSerializer
from utils.utils import tokenValidation


class SemesterResultView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        registration_no = request.query_params.get("registration_no")
        semester_id = request.query_params.get("semester_id")

        # check user need CGPA or GPA
        if semester_id not in ["FINAL", "Final", "final"]:

            student_data = get_object_or_404(UserAccount, username=registration_no)

            total_courses = get_object_or_404(Semester, id=semester_id)
            total_courses = total_courses.total_courses

            marks = get_list_or_404(Mark, examination__semester__id=semester_id, examination__name="final")

            if total_courses == len(marks):
                total_points = Mark.objects.filter(examination__semester__id=semester_id, examination__name="final").aggregate(total_points=Sum('mark'))['total_points']

                semester_point = total_points / total_courses

                create_GPA = {
                    "semester": semester_id,
                    "student": student_data.id,
                    "point": semester_point
                }

                is_result = GPA.objects.filter(student__username=registration_no, semester__id=semester_id).exists()

                create_GPA_serializer = SemesterResultCreateSerializer(data=create_GPA)
                if create_GPA_serializer.is_valid() and is_result is False:
                    create_GPA_serializer.save()

                marks_serializer = MarkEachCourseSerializer(marks, many=True)

                result = {
                    "first_name": student_data.first_name,
                    "last_name": student_data.last_name,
                    "registration": student_data.username,
                    "roll": student_data.roll,
                    "GPA": semester_point,            
                    "course_wise": marks_serializer.data,
                    "date": datetime.now().date()
                }
                return Response(result)
            
            return Response("not found")
        else:
            student_data = get_object_or_404(UserAccount, username=registration_no)
            result = GPA.objects.filter(student__username=registration_no)
            total_point = result.aggregate(total_point=Sum("point"))["total_point"]
            total_passed_semester = result.aggregate(total_passed_semester=Count("id"))["total_passed_semester"]
            serializer = SemesterResultSerializer(result, many=True)
            if total_passed_semester == 8:
                result = {
                    "first_name": student_data.first_name,
                    "last_name": student_data.last_name,
                    "registration": student_data.username,
                    "roll": student_data.roll,
                    "CGPA": total_point/8,            
                    "semester_wise": serializer.data,
                    "date": datetime.now().date()
                }
                return Response(result)
            return Response("not found")


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
                "CGPA": total_point/8,            
                "semester_wise": serializer.data,
                "date": datetime.now().date()
            }
            return Response(result)
        
        return Response("not found")
