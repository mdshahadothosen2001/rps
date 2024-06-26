from django.shortcuts import get_object_or_404
from django.db.models import Sum 

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import UserAccount
from mark.models import Mark
from semester.models import Semester
from ..serializers.result import MarkEachCourseSerializer, GPACalculatingSerializer


class MarkEachCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student_registration = request.data.get("student_registration")
        student = get_object_or_404(UserAccount, username=student_registration)
        data = request.data
        data["student"] = student.id
        serializers = MarkEachCourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("success")
        
        return Response("unsucess")
    

class GPACalculateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student_registration = request.data.get("student_registration")
        semester_id = request.data.get("semester_id")
        student = get_object_or_404(UserAccount, username=student_registration)

        total_courses = get_object_or_404(Semester, id=semester_id)

        marks = Mark.objects.filter(student__id=student.id, examination__name="final").aggregate(marks=Sum("mark"))["marks"]
        marks = marks / total_courses.total_courses
        data = {
            "semester": semester_id,
            "student": student.id,
            "point": marks
        }
        serializers = GPACalculatingSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response("success")
        else:
            return Response(serializers.errors)
        
        return Response("unsucess")   
