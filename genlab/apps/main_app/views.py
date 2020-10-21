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
        news = News.objects.all()
        return render(request, 'home.html', {
            'slides': slides,
            'researches': researches,
            'questions': questions,
            'news': news,
        })


class ResearchesView(View):

    def get(self, request):
        slides = HeaderSlid.objects.filter(page='researches')


        context={
            'slides':slides,
        }
        return render(request, 'researches.html', context)


class QuestionsView(View):

    def get(self, request):
        slides = HeaderSlid.objects.filter(page='questions')
        questions = QuestionsAnswers.objects.all()

        context={
            'slides':slides,
            'questions': questions,
        }

        return render(request, 'questions.html', context)

class CooperationView(View):

    
    def get(self, request):
        cards = About.objects.all()
        slides = HeaderSlid.objects.filter(page='cooperation')
        context = {
            'cards': cards,
            'slides': slides,
        }
        return render(request, 'cooperation.html', context)

