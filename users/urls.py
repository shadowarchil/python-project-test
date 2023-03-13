from django.urls import path
from users.views import CustomLoginView, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('sign-in/', CustomLoginView.as_view(), name='sign-in'),
    path('sign-out/', CustomLogoutView.as_view(), name='sign-out')
    
]
