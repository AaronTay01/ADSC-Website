# Generated by Django 4.1.7 on 2023-03-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0042_remove_answer_answer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ManyToManyField(blank=True, null=True, to='webapp.survey'),
        ),
    ]
