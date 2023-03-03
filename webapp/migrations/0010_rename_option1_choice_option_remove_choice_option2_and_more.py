# Generated by Django 4.1.7 on 2023-03-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_rename_author_project_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='option1',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='option4',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='webapp.question'),
        ),
    ]
