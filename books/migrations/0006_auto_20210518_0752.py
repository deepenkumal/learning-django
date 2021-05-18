# Generated by Django 3.1.5 on 2021-05-18 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0005_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]
