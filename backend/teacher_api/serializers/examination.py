from rest_framework import serializers

from exam.models import Examination

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ["id", 
                  "name",
                  "course",
                  "semester",
                  "teacher",
                  "deadline",
                  "question",
                ]
