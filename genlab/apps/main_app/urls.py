from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    
    path('researches/', views.ResearchesView.as_view(), name='researches' ),
    path('research/<slug:slug>', views.ResearchTypeView.as_view(), name='research-type'),
    path('questions/', views.QuestionsView.as_view(), name='questions' ),
    path('cooperations/', views.CooperationView.as_view(), name='cooperation' ),
    path('search.json/', views.Serach.as_view(), name='search' ),
    path('search/', views.SerachType.as_view(), name='search-type' ),
    path('news/', views.NewsView.as_view(), name='news' ),
    path('about/', views.AboutUsView.as_view(), name='about' ),


    path('feedback/', views.FeedbackView.as_view(), name='feedback' ), 
    path('research-application/', views.ResearchApplicationView.as_view(), name='research-application' ),
    path('users-questions/', views.UsersQuestionsView.as_view(), name='users-questions' ),
    path('subscriptions/', views.SubscriptionsView.as_view(), name='subscriptions' ),
    

    path('NotFound/', views.SorryView.as_view(), name='sorry' ),

]