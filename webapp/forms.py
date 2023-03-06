from django import forms
from django.contrib.auth.models import User

from .models import Project, Question, Choice, Answer
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

class QuestionaireForm(forms.Form):
    question_1 = forms.ChoiceField(widget=forms.RadioSelect,
                                   choices=())

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        del self.fields["question_1"]
        for question in question.objects.all():
            choices = [(choice.id, choice.option) for choice in question.choice_set.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
            self.fields[f"question_{question.id}"].label = question.question_text

    def save(self):
        # save as questionaire together with project id
        data = self.cleaned_data
        answer = Answer(project=self.project)
        answer.save()
        for question in self.project.question_set.all():
            choice = Choice.objects.get(pk=data[f"question_{question.id}"])
            answer.add(choice)

        answer.save()
        return answer


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
