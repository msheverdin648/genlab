from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from .models import (
    ResearchMethod,
    ResearchType,
    Research,
    HeaderSlid,
    QuestionsAnswers,
    About,
    Partners,
    News,
    )


#Как появятся все странички, убрать
#--------------------------------------------------------
class SorryView(View):
    
    def get(self, request):
        return render(request, 'sorry.html', {})
#--------------------------------------------------------


class HomeView(View):

    def get(self, request):

        slides = HeaderSlid.objects.filter(page='home')
        researches = Research.objects.all()
        questions = QuestionsAnswers.objects.filter(show_home=True)
        return render(request, 'home.html', {
            slides: 'slides',
            researches: 'researches',
            questions: 'questions',
        })


class ResearchesView(View):

    def get(self, request):
        return render(request, 'researches.html')


class QuestionsView(View):

    def get(self, request):
        return render(request, 'questions.html')

class CooperationView(View):

    def get(self, request):
        return render(request, 'cooperation.html')

