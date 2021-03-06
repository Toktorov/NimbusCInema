# Generated by Django 2.2.6 on 2021-07-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_url_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailer', models.FileField(null=True, upload_to='trailers/', verbose_name='Трейлер')),
                ('film', models.FileField(null=True, upload_to='videos/', verbose_name='Видео')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='url_trailer',
        ),
    ]
