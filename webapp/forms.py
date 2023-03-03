from django import forms
from django.contrib.auth.models import User

from .models import Project, Question, Choice
from django.forms.models import inlineformset_factory, ModelForm


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "description",
        )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (

        )

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('primary',)


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ('primary',)

# ProjectFormSet = inlineformset_factory(
#     User,
#     Project,
#     ProjectForm,
#     can_delete=False,
#     min_num=1,
#     extra=0,
# )
