# Generated by Django 4.0.6 on 2022-07-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=122, null=True, unique=True)),
                ('desc', models.TextField(max_length=200, null=True)),
                ('answer', models.TextField(max_length=200, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]