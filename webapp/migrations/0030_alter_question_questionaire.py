# Generated by Django 4.1.7 on 2023-03-06 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_alter_choice_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='questionaire', to='webapp.questionaire'),
        ),
    ]