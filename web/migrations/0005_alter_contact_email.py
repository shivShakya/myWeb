# Generated by Django 4.0.6 on 2022-07-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_contact_phone_alter_contact_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122, null=True),
        ),
    ]
