# Generated by Django 3.1.2 on 2022-11-19 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20221119_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
    ]
