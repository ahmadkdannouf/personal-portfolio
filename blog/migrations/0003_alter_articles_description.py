# Generated by Django 4.0 on 2022-01-05 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_articles_url_articles_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(max_length=100000),
        ),
    ]
