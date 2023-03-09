from django.contrib import admin
from webapp.models import Project, Question, Choice, Answer, Response


# class QuestionaireInLineAdmin(admin.TabularInline):
#     model = Questionaire
#     min_num = 1
#     can_delete = True


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


class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInLineAdmin]


admin.site.register(Project)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Questionaire, QuestionaireAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Answer)
