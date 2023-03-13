from django.urls import path
from users.views import CustomLoginView, CustomLogoutView, UserSignUpView

app_name = 'users'

urlpatterns = [
    path('sign-in/', CustomLoginView.as_view(), name='sign-in'),
    path('sign-out/', CustomLogoutView.as_view(), name='sign-out'),
    path('sign-up/', UserSignUpView.as_view(), name='sign-up'),
]
