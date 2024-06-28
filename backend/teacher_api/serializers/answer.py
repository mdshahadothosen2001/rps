from rest_framework import serializers

from answer.models import Answer


class AnswerListSerializer(serializers.ModelSerializer):
    examination_id = serializers.CharField(source="examination.id", read_only=True)
    examination_name = serializers.CharField(source="examination.name", read_only=True)
    student_registration = serializers.CharField(source="student.username", read_only=True)
    class Meta:
        model = Answer
        fields = [
            "examination_id",
            "examination_name",
            "student_registration",
            "answer",
        ]
