# Generated by Django 4.2.7 on 2025-05-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_user_auth0_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth0_user_id',
            field=models.CharField(blank=True, max_length=2048, null=True, unique=True),
        ),
    ]
