# Generated by Django 4.2.7 on 2025-05-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_user_auth0_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture_url',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]
