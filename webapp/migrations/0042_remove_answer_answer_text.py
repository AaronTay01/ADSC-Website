# Generated by Django 4.1.7 on 2023-03-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0041_answer_answer_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_text',
        ),
    ]
