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
