from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from .models import (
    ResearchMethod,
    ResearchType,
    Research,
    MainResearches,
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
        main_researches = MainResearches.objects.all()
        return render(request, 'home.html', {
            'slides': slides,
            'researches': researches,
            'questions': questions,
            'news': news,
            'main_researches': main_researches
        })


class ResearchesView(View):

    def get(self, request):
        slides = HeaderSlid.objects.filter(page='researches')
        researches = Research.objects.all()

        context={
            'slides':slides,
            'researches': researches,
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

class SerachView(ListView):

    def get_queryset(self):
        return ResearchType.objects.filter(name__incontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get('q')
        return context
    

