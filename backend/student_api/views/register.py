from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from ..serializers.register import UserRegistrationSerializer
from user.models import UserAccount


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def validate_parameter(self, username, password):
        if username and password:
            return True
        else:
            return False

    def have_account(self, username):
        is_member = UserAccount.objects.filter(username=username).exists()
        return is_member

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")
        roll = password

        if self.validate_parameter(username, password) is True:
            if self.have_account(username) is True:
                return Response("You have already account")
            user_data = {
                "username": username,
                "roll": roll,
                "phone_number": phone_number,
                "email": email,
                "password": password,
                "is_student": True,
                "is_active": True
            }

            serializer = UserRegistrationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()

                return Response("Completed your registration process!")

        return Response("Incompleted registration! Please provide valid data")
