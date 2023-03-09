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
            "project_status",
        )


# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = (
#
#         )

def intersect(list1, list2):
    sorted(list1)
    sorted(list2)

    list3 = set(list1).intersection(list2)

    # print(list3)
    return list3


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

        answers = survey.answer_set.first()
        selected_choices = {} if answers is None else [(selected_choice.id, selected_choice.option)
                                                       for selected_choice in
                                                       answers.answer_choice.all()]

        for question in survey.question_set.all():
            field_name = f"question_{question.id}"
            choices = [(choice.id, choice.option) for choice in question.choice_set.all()]
            question_selected_choice = intersect(selected_choices, choices)
            if question.type_question == question.TYPE_QUESTION_MULTIPLE_CHOICE:
                self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect,
                                                                           choices=choices)
                self.fields[f"question_{question.id}"].initial = question_selected_choice.pop() \
                    if question_selected_choice else None

            elif question.type_question == question.TYPE_QUESTION_CHECKBOX:
                self.fields[field_name] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                    choices=choices)
                if question_selected_choice:
                    choices = [(item[0]) for item in question_selected_choice]
                    self.fields[f"question_{question.id}"].initial = choices
            else:
                self.fields[field_name] = forms.CharField(widget=forms.TextInput)

            self.fields[field_name].label = question.question_text

    def save(self):
        data = self.cleaned_data
        survey_object = get_object_or_404(Survey, id=self.survey.id)
        # print(object_survey.answer_set.all())

        answer = survey_object.answer_set.first()
        answer.answer_choice.clear() if answer is not None else False

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
