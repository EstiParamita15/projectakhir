# Generated by Django 5.1.4 on 2024-12-23 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyu_app', '0004_remove_userprofileinfo_portfolio_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='full_name',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='kelas',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]