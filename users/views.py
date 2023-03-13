from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import UserCreateForm

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'auth/sign_in.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('core:home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:home')


class UserSignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('core:home')
    

