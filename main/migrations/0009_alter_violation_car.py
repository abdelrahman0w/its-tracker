# Generated by Django 3.2.3 on 2021-06-13 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210613_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.car'),
        ),
    ]
