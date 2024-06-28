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


class ExaminationDetailSerializer(serializers.ModelSerializer):
    exam_id = serializers.CharField(source="id", read_only=True)
    class Meta:
        model = Examination
        fields = ["exam_id", 
                  "name",
                  "course",
                  "semester",
                  "teacher",
                  "deadline",
                  "question",
                ]
