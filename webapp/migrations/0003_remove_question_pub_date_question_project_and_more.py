# Generated by Django 4.1.7 on 2023-02-27 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_project_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='webapp.project'),
        ),
        migrations.AddField(
            model_name='question',
            name='type_question',
            field=models.CharField(choices=[('Text', 'Text'), ('Date', 'Date'), ('Date Range', 'Date Range'), ('Multiple Choice', 'Multiple Choice')], default='TEXT', max_length=255),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
