from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Question
from core.forms import QuestionCreateForm
from django.urls import reverse_lazy
from typing import Dict, Any


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', context={
        'questions': Question.objects.all()
    })

class HomeView(ListView):
    template_name = 'home.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'
    ordering = ['-create_time']


class QuestionDetailView(DetailView):
    template_name = 'question_detail.html'
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'question_create.html'
    success_url = reverse_lazy('core:home')

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
