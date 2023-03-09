# Generated by Django 4.1.7 on 2023-03-09 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_answer_answer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='question', to='webapp.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.ManyToManyField(blank=True, to='webapp.choice'),
        ),
    ]