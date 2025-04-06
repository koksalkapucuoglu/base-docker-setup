# Generated by Django 5.2 on 2025-04-05 20:07

from django.db import migrations, models
import django_mongodb_backend.fields.auto


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPair',
            fields=[
                ('id', django_mongodb_backend.fields.ObjectIdAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('result', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
