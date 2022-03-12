# Generated by Django 3.2 on 2022-03-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220311_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]