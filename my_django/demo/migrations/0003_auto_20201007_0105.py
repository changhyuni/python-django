# Generated by Django 3.1.1 on 2020-10-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20201007_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
    ]
