# Generated by Django 3.1 on 2021-02-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
