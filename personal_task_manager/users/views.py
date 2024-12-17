from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from personal_task_manager.dashboard.models import CustomUser
from personal_task_manager.users.forms import RegistrationForm, UpdateProfileForm


# Create your views here.
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name= 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class EditProfileView(UpdateView):
    model = CustomUser
    template_name= 'users/update-profile.html'
    form_class = UpdateProfileForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

class RegisterView(CreateView):
    model= CustomUser
    template_name = 'users/register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        custom_user = form.save()
        login(self.request, custom_user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class MyLoginView(LoginView):
    template_name = 'users/login.html'

class MyLogoutView(LogoutView):
    template_name = 'users/logout.html'