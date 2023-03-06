from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    PROJECT_STATUS_CHOICES = [
        ('PD', 'Pending'),
        ('CP', 'Completed'),
        ('IP', 'In Progress'),
        ('DP', 'Dropped'),
    ]

    project_status = models.CharField(
        max_length=2,
        choices=PROJECT_STATUS_CHOICES,
        default='Pending',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-project', kwargs={'pk': self.pk})


# class Questionaire(models.Model):
#     title = models.CharField(max_length=100)
#
#     # def __str__(self):
#     #     self.title


class Question(models.Model):
    TYPE_QUESTION_CHECKBOX = 'Multiple Choice Checkbox'
    TYPE_QUESTION_FIELD = 'Field'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_CHECKBOX, "Multiple Choice Checkbox"),
        (TYPE_QUESTION_FIELD, "Field"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )
    # questionaire = models.ForeignKey(Questionaire, related_name="questionaire", null=True, blank=True,
    #                                  on_delete=models.PROTECT)
    question_text = models.CharField(max_length=200)
    type_question = models.CharField(max_length=255, choices=TYPE_QUESTION, default='TEXT')

    def __str__(self):
        return self.question_text


# Each question can have multiple Choices
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question.question_text}:{self.option}"


# Each questionaire has multiple questions & belong to a project
class Answer(models.Model):
    project = models.ForeignKey(Project, related_name="project", on_delete=models.PROTECT)
    # questionaire = models.ForeignKey(Questionaire, related_name="questionaire", on_delete=models.PROTECT)
    question = models.ForeignKey(Question, related_name="question", null=True, blank=True, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name="choice", null=True, blank=True, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.project.title}:{self.question.question_text}:{self.answer_text}"

# QUESTIONS = [{"What is the type of data used in this application?":["Personally Identifiable Information",
# "Location", 'Health Records', 'Grants and Subsidies '], "What is the type of data used in this application?
# Multiple options can be selected" "What is the sensitivity level of this data type?", "What are the user roles for
# the application?", "Which data does the user has access to?", "What operations are allowed on that data by that
# user?" }]

# QUESTION_CHOICES = []
