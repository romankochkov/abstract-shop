# Generated by Django 3.2.25 on 2024-06-14 05:35

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_books_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='cover',
            field=models.CharField(choices=[('SOFT', 'Мягкий'), ('SOLID', 'Твердый')], default='SOFT', max_length=5, verbose_name='Переплет'),
        ),
        migrations.AlterField(
            model_name='books',
            name='language',
            field=models.CharField(choices=[('RU', 'Русский'), ('UK', 'Украинский'), ('EN', 'Английский'), ('DE', 'Немецкий'), ('FR', 'Французский'), ('ES', 'Испанский')], default='RU', max_length=2, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(blank=True, upload_to=catalog.models.path_and_rename, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Тег'),
        ),
    ]
