# Generated by Django 4.0.2 on 2022-03-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_ratings_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]