# Generated by Django 5.0.4 on 2024-04-05 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_remove_user_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='start_date',
        ),
    ]