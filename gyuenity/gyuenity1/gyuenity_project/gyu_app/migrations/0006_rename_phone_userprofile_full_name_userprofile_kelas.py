# Generated by Django 5.1.4 on 2024-12-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyu_app', '0005_rename_full_name_userprofile_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='kelas',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
