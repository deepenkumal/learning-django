# Generated by Django 3.1.5 on 2021-05-18 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210518_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_profile',
            new_name='userprofile',
        ),
    ]