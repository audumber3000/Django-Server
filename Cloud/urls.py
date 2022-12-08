from django.urls import path

from . import views


urlpatterns = [
    path('file/upload', views.ProfileView.as_view(), name='profile'),
    path('file/download', views.ProfileView.as_view(), name='profile'),
    path('file/update', views.ProfileView.as_view(), name='profile'),
]
