# Generated by Django 4.0.2 on 2022-02-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('RU', 'Русский'), ('UK', 'Украинский'), ('EN', 'Английский'), ('DE', 'Немецкий'), ('FR', 'Французский')], max_length=2)),
                ('date', models.CharField(default='Неизвестно', max_length=20, null=True)),
                ('presence', models.BooleanField(default=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='catalog.Tags')),
            ],
        ),
    ]
