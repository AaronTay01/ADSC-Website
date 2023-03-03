from django.contrib import admin
from webapp.models import Project, Question, Choice, Answer


class AnswerInLineAdmin(admin.TabularInline):
    model = Answer


class ProjectAdmin(admin.ModelAdmin):
    inlines = [AnswerInLineAdmin]


class ChoiceInLineAdmin(admin.TabularInline):
    model = Choice
    max_num = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLineAdmin]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
