from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from webapp.views import dashboard, questionaire, project
from webapp.views.project import (
    # detail_project,
    # delete_project,
    # update_project
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

from webapp.views.dashboard import (
    ProjectListView
)
# from webapp.views.questionaire import (
#     QuestionCreateView
# )

urlpatterns = [
                  path('', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
                  path('dashboard/', ProjectListView.as_view(), name='dashboard'),
                  path('project/new/', ProjectCreateView.as_view(), name='create-project'),
                  path('project/<pk>/', ProjectDetailView.as_view(), name='detail-project'),
                  path('project/<pk>/update/', ProjectUpdateView.as_view(), name='update-project'),
                  path('project/<pk>/delete/', ProjectDeleteView.as_view(), name='delete-project'),
                  # path('htmx/project/<pk>/delete/', delete_project, name='delete-project'),
                  # path('htmx/project/<pk>/update/', update_project, name='update-project'),
                  path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
                  path('admin/', admin.site.urls),
                  # path('questionaire/<pk>/new', QuestionCreateView.as_view(), name='create-questionaire'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
