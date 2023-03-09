from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    TYPE_PROJECT_PENDING = 'PD'
    TYPE_PROJECT_COMPLETED = 'CP'
    TYPE_PROJECT_IN_PROGRESS = 'IP'
    TYPE_PROJECT_DROPPED = 'DP'

    PROJECT_STATUS_CHOICES = [
        (TYPE_PROJECT_PENDING, 'Pending'),
        (TYPE_PROJECT_COMPLETED, 'Completed'),
        (TYPE_PROJECT_IN_PROGRESS, 'In Progress'),
        (TYPE_PROJECT_DROPPED, 'Dropped'),
    ]

    project_status = models.CharField(
        max_length=2,
        choices=PROJECT_STATUS_CHOICES,
        default=TYPE_PROJECT_PENDING,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-project', kwargs={'pk': self.pk})


class Survey(models.Model):
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.title}:"


class Question(models.Model):
    TYPE_QUESTION_CHECKBOX = 'Multiple Choice Checkbox'
    TYPE_QUESTION_FIELD = 'Field'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_CHECKBOX, "Multiple Choice Checkbox"),
        (TYPE_QUESTION_FIELD, "Field"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )
    survey = models.ManyToManyField(Survey, blank=True)
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
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, related_name="question", null=True, blank=True, on_delete=models.PROTECT)
    # choice = models.ForeignKey(Choice, related_name="choice", null=True, blank=True, on_delete=models.PROTECT)
    # answer_text = models.CharField(max_length=100, null=True, blank=True)
    answer_choice = models.ManyToManyField(Choice, blank=True)

    # def __str__(self):
    #     return self.response.id
    # return f"{self.project.title}:{self.question.question_text}:{self.answer_text}"

# QUESTIONS = [{"What is the type of data used in this application?":["Personally Identifiable Information",
# "Location", 'Health Records', 'Grants and Subsidies '], "What is the type of data used in this application?
# Multiple options can be selected" "What is the sensitivity level of this data type?", "What are the user roles for
# the application?", "Which data does the user has access to?", "What operations are allowed on that data by that
# user?" }]

# QUESTION_CHOICES = []
