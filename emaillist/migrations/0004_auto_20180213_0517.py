# Generated by Django 2.0.2 on 2018-02-13 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emaillist', '0003_auto_20180213_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='university_name',
            new_name='name',
        ),
    ]