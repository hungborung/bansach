# Generated by Django 3.1 on 2021-01-13 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210113_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'cat_parent')},
        ),
    ]
