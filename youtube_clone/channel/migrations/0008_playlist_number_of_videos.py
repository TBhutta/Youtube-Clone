# Generated by Django 5.1.5 on 2025-04-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0007_video_restriction_video_type_video_visibility"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="number_of_videos",
            field=models.IntegerField(default=0),
        ),
    ]
