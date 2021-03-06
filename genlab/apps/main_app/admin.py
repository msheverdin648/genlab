from django.contrib import admin
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
    UsersQuestions,
    ResearchApplication
    )



admin.site.register(ResearchMethod)
admin.site.register(ResearchType)
admin.site.register(Research)
admin.site.register(MainResearches)
admin.site.register(HeaderSlid)
admin.site.register(QuestionsAnswers)
admin.site.register(About)
admin.site.register(Partners)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(UsersQuestions)
admin.site.register(ResearchApplication)