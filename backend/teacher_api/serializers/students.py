from rest_framework import serializers

from semester.models import Semester

class StudentListSerializer(serializers.ModelSerializer):
    registration = serializers.CharField(source="students.username", read_only=True)
    first_name = serializers.CharField(source="students.first_name", read_only=True)
    last_name = serializers.CharField(source="students.last_name", read_only=True)
    class Meta:
        model = Semester
        fields = [
            "id", 
            "registration",
            "first_name",
            "last_name",
            "session",
            "department",
        ]
