from django.contrib import admin
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



admin.site.register(ResearchMethod)
admin.site.register(ResearchType)
admin.site.register(Research)
admin.site.register(HeaderSlid)
admin.site.register(QuestionsAnswers)
admin.site.register(About)
admin.site.register(Partners)
admin.site.register(News)