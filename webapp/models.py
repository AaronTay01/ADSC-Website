from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
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

    def getQuestionText(self):
        return self.Question.question_text


class Question(models.Model):
    TYPE_QUESTION_CHECKBOX = 'Multiple Choice Checkbox'
    TYPE_QUESTION_FIELD = 'Field'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_CHECKBOX, "Multiple Choice Checkbox"),
        (TYPE_QUESTION_FIELD, "Field"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )

    question_text = models.CharField(max_length=200)
    type_question = models.CharField(max_length=255, choices=TYPE_QUESTION, default='TEXT')

    option1 = models.CharField(max_length=100, null=True, blank=True)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="question_choice", on_delete=models.CASCADE)
    option = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question.question_text


class Answer(models.Model):
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question.question_text

# class Questionaire(models.Model):
#     TYPE_QUESTION_CHECKBOX = 'Multiple Choice Checkbox'
#     TYPE_QUESTION_FIELD = 'Field'
#     TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

# def __str__(self):
#     return self.question.question_text
#
#     TYPE_QUESTION = (
#         (TYPE_QUESTION_CHECKBOX, "Multiple Choice Checkbox"),
#         (TYPE_QUESTION_FIELD, "Field"),
#         (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
#     )
#
#
#     question_text = models.CharField(max_length=200)
#     type_question = models.CharField(max_length=255, choices=TYPE_QUESTION, default='TEXT')
#     option1 = models.CharField(max_length=100, null=True)
#     option2 = models.CharField(max_length=100, null=True)
#     option3 = models.CharField(max_length=100, null=True)
#     option4 = models.CharField(max_length=100, null=True)

# QUESTIONS = [{"What is the type of data used in this application?":["Personally Identifiable Information","Location", 'Health Records', 'Grants and Subsidies
# '],
#              "What is the type of data used in this application? Multiple options can be selected"
#              "What is the sensitivity level of this data type?",
#              "What are the user roles for the application?",
#              "Which data does the user has access to?",
#              "What operations are allowed on that data by that user?"
#               }]

# QUESTION_CHOICES = []
