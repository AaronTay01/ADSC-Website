# Generated by Django 4.1.7 on 2023-03-06 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_alter_answer_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questionaire', to='webapp.questionaire'),
        ),
    ]