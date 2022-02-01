# Generated by Django 4.0.1 on 2022-02-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna',
            name='question',
        ),
        migrations.AddField(
            model_name='qna',
            name='question',
            field=models.ManyToManyField(to='assessment.Question'),
        ),
        migrations.RemoveField(
            model_name='qna',
            name='student_ans',
        ),
        migrations.AddField(
            model_name='qna',
            name='student_ans',
            field=models.ManyToManyField(to='assessment.Answer'),
        ),
    ]
