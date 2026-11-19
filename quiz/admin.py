from django.contrib import admin
from .models import Course, Quiz, Question, AnswerOption, Attempt, Response
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(Attempt)
admin.site.register(Response)
