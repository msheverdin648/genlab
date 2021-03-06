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
    ResearchApplication,
    UsersQuestions,
    Subscriptions
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



class NewsView(View):

    def get(self, request, *args, **kwargs):

        news = News.objects.all()
        slides = HeaderSlid.objects.filter(page='home')
        questions = QuestionsAnswers.objects.filter(show_home=True)
        context = {
            'news': news,
            'slides': slides,
            'questions': questions,
        }
        return render(request, "news.html", context)
    

        
class AboutUsView(View):

    def get(self, request, *args, **kwargs):

        slides = HeaderSlid.objects.filter(page='about')
        cards = About.objects.all()
        news = News.objects.all()
        context = {
            'news': news,
            'cards': cards,
            'slides' : slides,
        }
        return render(request, "about_us.html", context)



class FeedbackView(View):

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        author = request.POST.get('name')
        feedback = Feedback.objects.create(
            name=author, email=email, phone=user_phone
        )
        feedback.save()
        return HttpResponseRedirect('/')



class ResearchApplicationView(View):

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        user_phone = request.POST.get('phone')
        author = request.POST.get('name')
        research = request.POST.get('research')
        research_application = ResearchApplication.objects.create(
            name=author, text=text, phone=user_phone, research=research
        )
        research_application.save()
        return HttpResponseRedirect('/')

class UsersQuestionsView(View):

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        user_phone = request.POST.get('phone')
        author = request.POST.get('name')

        user_question = UsersQuestions.objects.create(
            name=author, text=text, phone=user_phone
        )
        user_question.save()
        return HttpResponseRedirect('/')


class SubscriptionsView(View):

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        message = Subscriptions.objects.create(
            email = email
        )
        message.save()
        return HttpResponseRedirect('/')
