from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from webapp.models import Project, Choice, Question

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)
#
#
# @login_required()
# def Questionaire(request):
#     context = {
#         'projects': Project.objects.all(),
#         'questionaire': Question.objects.all(),
#         'choice': Choice.objects.all()
#     }
#     return render(request, 'questionaire/questionaire.html', context)
#
#
# class QuestionDetailView(DetailView):
#     model = Question
#     template_name = "questionaire/project_detail.html"


# class QuestionCreateView(LoginRequiredMixin, CreateView):
#     model = Choice
#     template_name = "questionaire/questionaire.html"
#     fields = ['question_text', 'option1', 'option2', 'option3', 'option4']
#
#     def post(self, request, context):
#         if request.POST():
#             a_valid = form.is_valid()
#             b_valid = formB.is_valid()
#             c_valid = formC.is_valid()
#             # we do this since 'and' short circuits and we want to check to whole page for form errors
#             if a_valid and b_valid and c_valid:
#                 a = formA.save()
#                 b = formB.save(commit=False)
#                 c = formC.save(commit=False)
#                 b.foreignkeytoA = a
#                 b.save()
#                 c.foreignkeytoB = b
#                 c.save()
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#
# class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Question
#     template_name = "questionaire/create_question.html"
#     fields = ['title', 'description']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         project = self.get_object()
#         if self.request.user == project.user:
#             return True
#         return False
