# Generated by Django 3.1 on 2020-10-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200921_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupinfo',
            name='confpassword',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
