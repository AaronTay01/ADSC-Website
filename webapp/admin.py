from django.contrib import admin
from webapp.models import Project, Question, Choice, Answer, Survey


class ChoiceInLineAdmin(admin.TabularInline):
    model = Choice
    max_num = 4
    can_delete = True


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLineAdmin]


class QuestionInLineAdmin(admin.TabularInline):
    model = Question


class QuestionaireAdmin(admin.ModelAdmin):
    inlines = [QuestionInLineAdmin]


class AnswerInLineAdmin(admin.TabularInline):
    model = Answer
    max_num = 1


class ResponseInLineAdmin(admin.TabularInline):
    model = Answer


class SurveyAdmin(admin.ModelAdmin):
    inlines = [AnswerInLineAdmin]


admin.site.register(Project)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
