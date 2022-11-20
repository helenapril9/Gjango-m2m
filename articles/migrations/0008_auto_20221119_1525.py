# Generated by Django 3.1.2 on 2022-11-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_scope_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='Tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes1', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes1', to='articles.tag'),
        ),
    ]
