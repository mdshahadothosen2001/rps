from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.answer import AnswerSerializer
from utils.utils import tokenValidation


class AnswerSubmittionView(APIView):
    permission_classes = [IsAuthenticated]

    def validate_parameter(self, examination, stuend, answer):
        if examination and stuend and answer:
            return True
        else:
            return False

    def post(self, request):
        payload = tokenValidation(request)
        student_id = payload.get("id")
        examination = request.data.get("examination")
        answer = request.data.get("answer")

        if self.validate_parameter(examination, student_id, answer) is True:
            user_data = {
                "examination": examination,
                "student": student_id,
                "answer": answer,
            }

            serializer = AnswerSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()

                return Response("Submitted your answer paper!")

        return Response("Incompleted process! Please provide valid data")
