from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('researches/', views.ResearchesView.as_view(), name='researches' ),
    path('questions/', views.QuestionsView.as_view(), name='questions' ),
    path('cooperations/', views.CooperationView.as_view(), name='cooperation' ),




    path('NotFound/', views.SorryView.as_view(), name='sorry' ),
]