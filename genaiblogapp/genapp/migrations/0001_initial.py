# Generated by Django 5.1.5 on 2025-01-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Given_Input', models.CharField(max_length=300)),
                ('result', models.TextField()),
            ],
        ),
    ]
