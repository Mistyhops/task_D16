# Generated by Django 3.2.7 on 2021-09-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_alter_reply_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='is_accepted',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
