from django.shortcuts import get_list_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from answer.models import Answer
from ..serializers.answer import AnswerListSerializer
from utils.utils import tokenValidation


class AnswerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = tokenValidation(request)
        teacher_id = payload.get("id")
        semester_id = request.query_params.get("semester_id")
        examination_name = request.query_params.get("examination_name")
        if semester_id and examination_name:
            answers = get_list_or_404(Answer, examination__semester__id=semester_id, examination__name=examination_name)
            serializer = AnswerListSerializer(answers, many=True)
            return Response(serializer.data)
        
        answers = get_list_or_404(Answer, examination__teacher__id=teacher_id)
        serializer = AnswerListSerializer(answers, many=True)
        return Response(serializer.data)
