# Generated by Django 5.1.4 on 2024-12-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyu_app', '0008_progress_quizresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='class_number',
            field=models.IntegerField(choices=[(1, 'Kelas 1'), (2, 'Kelas 2'), (3, 'Kelas 3')], default=1),
        ),
    ]
