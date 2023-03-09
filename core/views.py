from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Question


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', context={
        'questions': Question.objects.all()
    })

class HomeView(ListView):
    template_name = 'home.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'


class QuestionDetailView(DetailView):
    template_name = 'question_detail.html'
    model = Question
