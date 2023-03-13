from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Question
from core.forms import QuestionCreateForm
from django.urls import reverse_lazy, reverse
from typing import Dict, Any


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', context={
        'questions': Question.objects.all()
    })


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'questions'
    ordering = ['-create_time']
    paginate_by = 5

    def get_queryset(self):
        queryset = Question.objects.filter(title__contains=self.request.GET.get('q', ''))
    
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


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

    def form_valid(self, form):
        self.object = form.save()
        self.object.tags.add(
            *[tag.id for tag in form.cleaned_data['tags']]
        )
        return super().form_valid(form)
        


class QuestonDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'question_delete.html'
    success_url = reverse_lazy('core:home')

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'question_update.html'
    fields = ['title', 'text']

    def get_success_url(self) -> str:
        return reverse('core:question-detail', kwargs={'pk': self.get_object().pk})

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

