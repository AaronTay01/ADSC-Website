# Generated by Django 4.1.7 on 2023-03-04 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_question_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.project'),
        ),
    ]