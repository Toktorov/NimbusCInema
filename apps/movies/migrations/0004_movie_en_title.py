# Generated by Django 2.2.6 on 2021-07-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210711_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='en_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
