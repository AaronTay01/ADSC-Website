# Generated by Django 4.1.7 on 2023-03-04 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_alter_answer_answer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_questionaire', to='webapp.questionaire'),
            preserve_default=False,
        ),
    ]
