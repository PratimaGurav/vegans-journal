# Generated by Django 3.2 on 2022-03-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_snippet',
            field=models.CharField(default='Click to Read the Blog Post', max_length=200),
        ),
    ]