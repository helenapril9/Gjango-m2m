# Generated by Django 3.1.2 on 2022-11-19 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_auto_20221119_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tag', to='articles.article')),
            ],
            options={
                'ordering': ['-is_main'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тег')),
                ('tags', models.ManyToManyField(through='articles.Scope', to='articles.Article')),
            ],
        ),
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tag', to='articles.tag'),
        ),
    ]