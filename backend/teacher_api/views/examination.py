from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers.examination import ExaminationSerializer
from utils.utils import tokenValidation


class ExaminationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        payload = tokenValidation(request)
        teacher_id = payload.get("id")
        data = request.data
        data['teacher'] = teacher_id
        serializers = ExaminationSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response("success")
        
        return Response("unsucess")
