from django.urls import path

from . import views

urlpatterns = [
    path('audumber/', views.index, name='index'),
]