from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exam.models import Examination
from ..serializers.examination import ExaminationSerializer


class ExaminationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        semester_id = request.query_params.get("semester_id")
        examinations = Examination.objects.filter(semester__id=semester_id)
        serializers = ExaminationSerializer(examinations, many=True)
        return Response(serializers.data)


class ExaminationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        examination_id = request.query_params.get("examination_id")
        examination = get_object_or_404(Examination, id=examination_id)
        serializers = ExaminationSerializer(examination)
        return Response(serializers.data)
