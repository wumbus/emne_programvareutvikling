# Generated by Django 4.0.2 on 2022-03-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_colormode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mode',
            field=models.BooleanField(default=False),
        ),
    ]
