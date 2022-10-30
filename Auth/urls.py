from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('login/' , views.Login.as_view() , name='old_user'),
    path('verify-otp/' , views.OtpVerification.as_view() , name='otp_verify'),
    path('register/', views.UserRegistration.as_view() , name='new_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]