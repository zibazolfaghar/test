# Generated by Django 3.1.1 on 2020-09-24 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200923_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
