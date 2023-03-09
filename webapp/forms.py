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

    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = questions
        del self.fields["question_1"]
        for question in questions.objects.all():
            field_name = f"question_{question.id}"
            if question.type_question == question.TYPE_QUESTION_MULTIPLE_CHOICE:
                choices = [(choice.id, choice.option) for choice in question.choice_set.all()]
                self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect,
                                                                           choices=choices)
            elif question.type_question == question.TYPE_QUESTION_CHECKBOX:
                choices = [(choice.id, choice.option) for choice in question.choice_set.all()]
                self.fields[field_name] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                    choices=choices)
            else:
                self.fields[field_name] = forms.CharField(widget=forms.TextInput)

            self.fields[field_name].label = question.question_text

    def save(self):
        data = self.cleaned_data
        answer = Answer(question=self.question)
        answer.save()
        for question in self.question.question_set.all():
            choice = Choice.objects.get(pk=data[f"question_{question.id}"])
            answer.answer.add(choice)

        print("hello")
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
