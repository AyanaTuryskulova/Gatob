# Generated by Django 5.0.4 on 2024-07-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_remove_news_likes_remove_news_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
