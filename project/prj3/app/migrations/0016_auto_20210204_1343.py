# Generated by Django 3.1 on 2021-02-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_product_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='num_visits',
            field=models.IntegerField(default=0),
        ),
    ]
