from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token
from Auth.views import  logout_view , add_user_info
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('verify-otp/' , views.OtpVerification.as_view(), name='otp_verify'),
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('add_info/', add_user_info , name='info')
]
