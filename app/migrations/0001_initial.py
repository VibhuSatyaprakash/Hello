# Generated by Django 3.2.8 on 2022-02-06 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
