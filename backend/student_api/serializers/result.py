from rest_framework import serializers

from gpa.models import GPA
from mark.models import Mark


class SemesterResultSerializer(serializers.ModelSerializer):
    semester_no = serializers.CharField(source='semester.semester_no', read_only=True)

    class Meta:
        model = GPA
        fields = [
            "semester_no",
            "point",
        ]

class MarkEachCourseSerializer(serializers.ModelSerializer):
    examination_course = serializers.CharField(source='examination.course', read_only=True)

    class Meta:
        model = Mark
        fields = [
            "examination_course",
            "mark",
        ]