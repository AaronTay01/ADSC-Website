from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Project, Question, Choice, Survey, Answer
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

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = (
        )
    # question_1 = forms.ChoiceField(widget=forms.RadioSelect,
    #                                choices=())

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        # del self.fields["question_1"]
        for question in survey.question_set.all():
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
        # TODO: get object instead of creating new

        object_survey = get_object_or_404(Survey, id=self.survey.id)
        # print(object_survey.answer_set.all())

        answer = object_survey.answer_set.first()
        if answer is None:
            answer = Answer(survey=self.survey)
            answer.save()

        for question in self.survey.question_set.all():
            if question.type_question == question.TYPE_QUESTION_MULTIPLE_CHOICE:
                choice = Choice.objects.get(pk=data[f"question_{question.id}"])
                answer.answer_choice.add(choice)
            if question.type_question == question.TYPE_QUESTION_CHECKBOX:
                for pk in data[f"question_{question.id}"]:
                    choice = Choice.objects.get(pk=pk)
                    answer.answer_choice.add(choice)
            # TODO: For CharField
            # else:
            #     print(data[f"question_{question.id}"])
            #     textAns = data[f"question_{question.id}"]
            #     answer.answer_text.add(textAns)

        answer.save()
        # return answer


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
