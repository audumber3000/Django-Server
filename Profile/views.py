from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from models import UserInformation
from rest_framework.response import Response

class ProfileView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        """
        Get the entire profile from DB using the Username (which is mobile number of user)
        """
        phone_number = request.body
        user_information = UserInformation().get_user_information(phone_number)
        data = {}
        if not user_information:
            data['status_code'] = 400
            data['status'] = "fail"
            data['error'] = "Something went wrong"
            data['message'] = "User profile information cant be fetched !"
        else:
            data['status_code'] = 200
            data['data'] = user_information
            data['status'] = "success"
            data['error'] = "Something went wrong"
            data['message'] = "User profile information cant be fetched !"

        return Response(data, status=status.HTTP_200_OK)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

