# Generated by Django 4.1.7 on 2023-03-04 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_alter_question_project_alter_questionaire_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='project',
        ),
        migrations.RemoveField(
            model_name='questionaire',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='questionaire',
            name='question',
        ),
        migrations.AlterField(
            model_name='choice',
            name='option',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='webapp.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='webapp.question')),
                ('questionaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionaire', to='webapp.questionaire')),
            ],
        ),
    ]