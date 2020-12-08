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
    path('feedback/', views.FeedbackView.as_view(), name='feedback' ),
    path('news/', views.NewsView.as_view(), name='news' ),


    path('NotFound/', views.SorryView.as_view(), name='sorry' ),

]