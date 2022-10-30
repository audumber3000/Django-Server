from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here

# from services import otp_service
from Auth.services import send_opt


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Login(APIView):

    def post(self , request):
        try :


            username = request.data.get("username")
            password = username+"123"
            email = username+"@gmail.com"
            user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password)

            token = Token.objects.create(user=user)
            print(token.key)
            otp_response = send_opt(username)
            res = {}
            if otp_response:
                res = {
                    "status_code": 200,
                    "data": {
                    "username": username,
                    },
                    "message":"Creating new user"
                }


            return Response(res, status=status.HTTP_200_OK)
        except :
            return Response("User already exits")


class UserRegistration(APIView):
    """
    this class is used for creating new users data to database and creating new user.
    """

    def post(self, request):

        return Response({"message": "function not yet implemented"})


class OtpVerification(APIView):
    """
    this class is used for verifying the OTP send by client
    username : ,
    OTP : ,
    """

    def post(self, request):

        return Response({"message": "function not yet implemented"})
