# Generated by Django 3.2.3 on 2021-06-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(db_index=True, max_length=10000, primary_key=True, serialize=False, unique=True, verbose_name='Car ID'),
        ),
    ]