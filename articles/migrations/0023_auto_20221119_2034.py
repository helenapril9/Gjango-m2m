# Generated by Django 3.1.2 on 2022-11-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20221119_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(through='articles.Scope', to='articles.Article'),
        ),
    ]
