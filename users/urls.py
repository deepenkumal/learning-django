from django.urls import path ,include
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/',views.SignupView.as_view() , name='signup'),
    path('profile/',views.ProfileView.as_view() , name='profile'),
]