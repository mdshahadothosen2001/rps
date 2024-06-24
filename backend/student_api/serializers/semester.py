from rest_framework import serializers

from semester.models import Semester

class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ["id", 
                  "semester_no",
                  "session",
                  "department",
                  "teachers",
                  "students",
                  "courses",
                  "total_courses",
                ]
