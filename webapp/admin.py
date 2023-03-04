from django.contrib import admin
from webapp.models import Project, Question, Choice, Questionaire


class AnswerInLineAdmin(admin.TabularInline):
    model = Questionaire


class ProjectAdmin(admin.ModelAdmin):
    inlines = [AnswerInLineAdmin]


class ChoiceInLineAdmin(admin.TabularInline):
    model = Choice
    min_num = 2
    max_num = 4
    can_delete = True


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLineAdmin]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
