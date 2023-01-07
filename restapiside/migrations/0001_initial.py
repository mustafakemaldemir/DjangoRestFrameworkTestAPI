# Generated by Django 4.1.5 on 2023-01-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('activity_status', models.BooleanField(max_length=150)),
                ('published_date', models.DateField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
