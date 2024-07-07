from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.SignUp.as_view(), name = 'signup'),
    path('dashboard/', views.MainView.as_view(), name='all'),
]