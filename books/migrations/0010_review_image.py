# Generated by Django 3.1.5 on 2021-05-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='Book/reviews'),
        ),
    ]
