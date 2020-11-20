from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.forms.models import model_to_dict
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
    Feedback,
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
        research_slugs = ResearchMethod.objects.all()

        return render(request, 'home.html', {
            'slides': slides,
            'researches': researches,
            'questions': questions,
            'news': news,
            'main_researches': main_researches,
            'research_slugs': research_slugs,
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

class ResearchTypeView(View):

    def get(self, request, *args, **kwargs):

        types = ResearchType.objects.get(slug=kwargs.get('slug'))

        context={
            'types': types,
        }
        return render(request, 'research-type.html', context)

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

'''
class Serach(ListView):

    def get(self, request):
        q = request.GET.get('q')
        types = ResearchType.objects.filter(name__icontains = q).distinct().values('name')
        a = list(types)
        return JsonResponse({'types': a}, safe=False)'''


class Serach(View):

    def get(self, request):
        q = request.GET.get('q')
        search_list = []
        types = ResearchType.objects.filter(name__icontains = q)
        if types:
            if not(q == " " or q == "") :
                for b in types:
                    new = {'type': b.name, 'slug': b.slug}
                    search_list.append(new)
                return JsonResponse({'types': search_list}, safe=False)

class SerachType(View):

    def get(self, request):
        q = request.GET.get('q')
        types = ResearchType.objects.filter(name__icontains = q).first()

        context = {
            'types': types,
        }

        return render(request, 'research-type.html', context)

class FeedbackView(View):

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        author = request.POST.get('name')
        message = Feedback.objects.create(
            name=author, email=email, phone=user_phone
        )
        message.save()
        return HttpResponseRedirect('/cooperations/')
    

        


