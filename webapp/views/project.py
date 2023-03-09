from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from webapp.models import Project, Question, Answer, Survey

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


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
        created = super().form_valid(form)
        Survey.objects.create(project_id=self.object.pk)  # Create empty Survey Instance
        questions = Question.objects.all()
        for question in questions:
            question.survey.add(self.object.pk)
            print(self.object.pk)
        return created


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "project/create_project.html"
    fields = ['title', 'description', 'project_status']

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
