# Generated by Django 3.2.7 on 2021-09-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0004_auto_20210902_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
