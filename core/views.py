from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from core.models import Question

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', context={
        'questions': Question.objects.all()
    })
