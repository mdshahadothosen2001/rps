from rest_framework.serializers import ModelSerializer

from answer.models import Answer


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "examination",
            "student",
            "answer",
        ]
