# Generated by Django 5.2 on 2025-04-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('result', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
