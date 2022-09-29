from django.urls import path
from . import views
app_name = 'profiles'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
