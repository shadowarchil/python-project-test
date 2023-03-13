from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'auth/sign_in.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('core:home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:home')

