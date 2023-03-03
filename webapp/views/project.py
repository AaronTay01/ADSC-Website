from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from webapp.forms import ProjectForm, ChoiceForm, QuestionForm
from webapp.models import Project, Question, Choice

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# @login_required()
# def CreateProject(request):
#     context = {
#         'questions': Question.objects.all()
#     }
#     return render(request, 'project/create_project.html', context)


# def create_project(request):
#     project_form = ProjectForm(request.POST, prefix="primary")
#     question_form = QuestionForm(request.POST, prefix="Question")
#     choice_form = ChoiceForm(request.POST, prefix="Choice")
#     if request.POST():
#         a_valid = project_form.is_valid()
#         b_valid = question_form.is_valid()
#         c_valid = choice_form.is_valid()
#         if a_valid and b_valid and c_valid:
#             a = formA.save()
#             b = formB.save(commit=False)
#             c = formC.save(commit=False)
#             b.foreignkeytoA = a
#             b.save()
#             c.foreignkeytoB = b
#             c.save()

    # return render_to_response('multi_model.html', {
    #     'primary_form': primary_form,
    #     'b_form': b_form,
    #     'c_form': c_form,
    # })


# @login_required()
# def create_project(request):
#     project = ProjectForm(request.POST or None)
#
#     if request.method == "POST":
#         if project.is_valid():
#             project = project.save(commit=False)
#             project.user = request.user
#             project.save()
#             messages.success(request, 'Project has been created')
#             return redirect("detail-project", pk=project.id)
#         else:
#             return render(request, "project/partials/project_form.html", {
#                 "project": project
#             })
#
#     context = {
#         "projectset": project
#     }
#
#     return render(request, 'project/create_project.html', context)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_detail.html"


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/dashboard'
    template_name = "project/project_delete.html"

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "project/create_project.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "project/create_project.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

# def detail_project(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {
#         "project": project
#     }
#     return render(request, "project/project_detail.html", context)

#
# def delete_project(request, pk):
#     project = Project.objects.get(pk=pk)
#     if request.method == "POST":
#         project.delete()
#         return HttpResponse("")
#
#     return HttpResponseNotAllowed(
#         [
#             "POST",
#         ]
#     )

# def update_project(request, pk):
#     project = Project.objects.get(pk=pk)
#     form = ProjectForm(request.POST or None, instance=project)
#
#     if request.method == "POST":
#         if project.is_valid():
#             project = project.save()
#             messages.success(request, 'Project has been created')
#             return redirect("detail-project", pk=project.id)
#
#     context = {
#         "form": form,
#         "project": project
#     }
#     return render(request, "project/partials/project_form.html", context)
