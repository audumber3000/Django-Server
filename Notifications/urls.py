from django.urls import path

from . import views


urlpatterns = [
    path('send-email/', views.ProfileView.as_view(), name='email'),

    path('send-sms/', views.ProfileView.as_view(), name='sms'),

    path('send-whatsapp/', views.ProfileView.as_view(), name='whatsapp'),

    path('send-app-notifications/', views.ProfileView.as_view(), name='notification'),
]
