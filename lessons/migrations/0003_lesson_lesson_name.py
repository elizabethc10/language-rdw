# Generated by Django 3.1.5 on 2022-01-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20211207_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_name',
            field=models.CharField(default='default lesson name', max_length=80),
            preserve_default=False,
        ),
    ]
