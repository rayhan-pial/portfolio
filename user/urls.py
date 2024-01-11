
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # Define your views and URLs here
    path('profile/', views.user_profile, name='user_profile'),
    # Add more paths as needed
]
