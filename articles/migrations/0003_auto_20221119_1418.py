# Generated by Django 3.1.2 on 2022-11-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(related_name='article', to='articles.Article'),
        ),
    ]
