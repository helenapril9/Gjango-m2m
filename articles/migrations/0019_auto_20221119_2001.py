# Generated by Django 3.1.2 on 2022-11-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20221119_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(related_name='article_tag_1', through='articles.Scope', to='articles.Article'),
        ),
    ]
