from django.test import TestCase
from .models import Video
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class VideoTestCase(TestCase):
    def setUp(self):
        Video.objects.create(video_file="/media/videos/video_files/feerger",
                             description="This is the description",
                             author=USER_MODEL.objects.filter(id=1).first(),
                             )

    def test_video_creation(self):
        video = Video.objects.get(id=2)
