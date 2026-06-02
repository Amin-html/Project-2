from django.urls import path
from . import views

urlpatterns = [
    path('', views.computer_list, name='computer_list'),
    path('<int:pk>/', views.computer_detail, name='computer_detail'),
]