# Generated by Django 3.2.4 on 2021-06-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]