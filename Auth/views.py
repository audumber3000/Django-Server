from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from Auth.services import send_otp, verify_otp
from Auth.serializers import RegistrationSerializer, UserInfoSerializer
from Auth import models
from django.contrib.auth.models import User
from django.core.cache import cache


#
class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        cache.set('my_key', 'hello, world!', 300)
        print(cache.get('my_key'))
        return Response(content)


#

#
#
class UserRegistration(APIView):
    """
    this class is used for creating new users data to database and creating new user.
    """

    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)

        data = {}
        sms_res = send_otp(request.data.get('username'))
        if not sms_res:
            data['status_code'] = 400
            data['status'] = "fail"
            data['error'] = "Invalid Number"
            data['message'] = "Registration Unsuccessful!"

            return Response(data, status=status.HTTP_201_CREATED)

        elif serializer.is_valid():
            account = serializer.save()

            token = Token.objects.get(user=account).key

            data['status_code'] = 200
            data['status'] = "success"
            data['data'] = {
                'username': account.username,
                'token': token
            }
            data['message'] = "Registration Successful!"
        else:

            data['status_code'] = 400
            data['status'] = "fail"
            data['error'] = serializer.errors
            data['message'] = "Registration Unsuccessful!"

        return Response(data, status=status.HTTP_201_CREATED)


class OtpVerification(APIView):
    """
    this class is used for verifying the OTP send by client
    username : ,
    OTP : ,
    """

    def post(self, request):

        response = verify_otp(request.data.get('username'), request.data.get('otp'))
        data = {}
        if response:
            data['status_code'] = 200
            data['status'] = "success"
            data['data'] = {}
            data['message'] = "Correct OTP"
        else:
            data['status_code'] = 400
            data['status'] = "fail"
            data['error'] = "Incorrect OTP"
            data['message'] = "Incorrect OTP"

        return Response(data, status=200)


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()  # check documnetation for these
        return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
def add_user_info(request):
    serializer = UserInfoSerializer(data=request.data)
    if serializer.is_valid():
        print("Entered into validation......")
        serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)
