# Generated by Django 4.1.7 on 2023-03-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_remove_answer_choice_remove_answer_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionaire',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='webapp.choice'),
        ),
    ]
