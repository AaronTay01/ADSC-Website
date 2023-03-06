from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProjectForm, QuestionForm, ChoiceForm, QuestionaireForm
from webapp.models import Project, Choice, Question, Answer

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)


def show_questionaire(request, pk):
    answer = get_object_or_404(Question, pk=pk)
    form = QuestionaireForm(Question)
    context = {
        "question": answer,
        "form": form
    }
    return render(request, "questionaire/questionaire.html", context)


def post_questionaire(request):
    if request.method == "POST":
        answerForm = QuestionaireForm(request.POST, instance=Questionaire())
    return render(request, "")


def create_question(request):
    if request.method == "POST":
        questionForm = QuestionForm(request.POST, instance=Question())
        choiceForms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice()) for x in range(0, 3)]
        if questionForm.is_valid() and all([cf.is_valid() for cf in choiceForms]):
            new_question = questionForm.save()
            for cf in choiceForms:
                new_choice = cf.save(commit=False)
                new_choice.poll = new_question
                new_choice.save()
            return HttpResponseRedirect('/question/add/')
        else:
            questionForm = QuestionForm(instance=Question())
            choiceForms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0, 3)]
        return render('create_question.html', {'question_form': questionForm, 'choice_forms': choiceForms})
