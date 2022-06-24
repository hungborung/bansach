# Generated by Django 3.1 on 2021-01-13 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210113_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.category'),
        ),
    ]