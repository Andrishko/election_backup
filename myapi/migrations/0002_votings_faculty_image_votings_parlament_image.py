# Generated by Django 4.1.5 on 2023-01-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votings',
            name='faculty_image',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AddField(
            model_name='votings',
            name='parlament_image',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]
