from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from personal_task_manager.users.views import ProfileDetailView, MyLoginView, MyLogoutView, RegisterView, \
    EditProfileView

urlpatterns = [
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='edit profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]