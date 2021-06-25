# Generated by Django 3.2.3 on 2021-06-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210619_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='additional',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='violation',
            name='comments',
            field=models.TextField(default='N/A', max_length=555),
        ),
    ]