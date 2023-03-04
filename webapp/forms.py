from django import forms
from django.contrib.auth.models import User

from .models import Project, Question, Choice, Questionaire
from django.forms.models import inlineformset_factory, ModelForm


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "description",
        )


# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = (
#
#         )

class QuestionaireForm(ModelForm):
    question_1 = forms.ChoiceField(widget=forms.RadioSelect,
                                   choices=())

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        del self.fields["question_1"]
        for question in question.question_set.all():
            choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
            self.fields[f"question_{question.id}"].label = question.question_text

    def save(self):
        data = self.cleaned_data
        questionaire = Questionaire(project=self.project)
        questionaire.save()
        for question in self.project.question_set.all():
            choice = Choice.objects.get(pk=data[f"question_{question.id}"])
            questionaire.answer.add(choice)

        questionaire.save()
        return questionaire


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('Project',)


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ('Question',)

# ProjectFormSet = inlineformset_factory(
#     User,
#     Project,
#     ProjectForm,
#     can_delete=False,
#     min_num=1,
#     extra=0,
# )
