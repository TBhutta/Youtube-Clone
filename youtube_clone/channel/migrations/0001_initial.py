# Generated by Django 5.1.5 on 2025-03-09 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("thumbnail", models.ImageField(upload_to="videos/thumbnails")),
                ("video_file", models.FileField(upload_to="videos/video_files/")),
                ("description", models.TextField()),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                ("author", models.IntegerField()),
                ("views", models.IntegerField(default=0)),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "videos",
            },
        ),
        migrations.CreateModel(
            name="User_Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("last_updated", models.DateField(auto_now=True)),
                (
                    "owner_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
                (
                    "commenter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "replying_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="channel.comment",
                    ),
                ),
                (
                    "video_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="channel.video"
                    ),
                ),
            ],
            options={
                "db_table": "comments",
            },
        ),
    ]
