from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'dashboard/dashboard.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']


@login_required()
def Dashboard(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)
