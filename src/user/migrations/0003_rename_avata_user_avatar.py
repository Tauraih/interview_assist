# Generated by Django 5.1.4 on 2024-12-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_avata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avata',
            new_name='avatar',
        ),
    ]
