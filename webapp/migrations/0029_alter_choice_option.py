# Generated by Django 4.1.7 on 2023-03-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0028_questionaire_title_alter_choice_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='option',
            field=models.CharField(max_length=100),
        ),
    ]