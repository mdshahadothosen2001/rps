from rest_framework import serializers

from answer.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    student_registration = serializers.CharField(source="student.username", read_only=True)
    class Meta:
        model = Answer
        fields = [
            "student_registration",
            "answer",
        ]
