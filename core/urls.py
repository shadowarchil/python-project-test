from django.urls import path
from core.views import HomeView, QuestionDetailView, QuestionCreateView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('ask/', QuestionCreateView.as_view(), name='question-create')
]