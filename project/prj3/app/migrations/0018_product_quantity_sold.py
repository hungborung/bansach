# Generated by Django 3.1 on 2021-02-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]