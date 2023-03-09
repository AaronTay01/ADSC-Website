from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import ProjectForm, QuestionForm, ChoiceForm, QuestionaireForm
from webapp.models import Project, Choice, Question, Answer, Survey

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)


def show_questionaire(request, pk):
    survey = get_object_or_404(Survey, pk=pk)  # get response instance where project.id equals to response.id

    post_data = request.POST if request.method == "POST" else None
    form = QuestionaireForm(survey, post_data, instance=survey)

    url = reverse("detail-project", args=(pk,))
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)

    context = {
        "survey": survey,
        "form": form,
    }
    return render(request, "questionaire/questionaire.html", context)


# def post_questionaire(request):
#     if request.method == "POST":
#         answerForm = QuestionaireForm(request.POST, instance=Response())
#     return render(request, "")


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
