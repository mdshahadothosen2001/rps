from rest_framework import serializers

from gpa.models import GPA
from mark.models import Mark


class MarkEachCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = [
            "examination",
            "student",
            "mark",
        ]


class GPACalculatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPA
        fields = [
            "semester",
            "student",
            "point",
        ]
