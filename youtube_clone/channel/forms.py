from django.forms import ModelForm
from .models import Video

# class VideoUploadForm(forms.Form):
#     title = forms.CharField(max_length=60)
#     thumbnail = forms.ImageField()
#     video_file = forms.FileField()
#     description = forms.Textarea()
#     upload_date = forms.DateTimeField(initial=datetime.today().isoformat) # TODO: Make readonly
#     author = forms.CharField() # TODO: Make readonly


class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ["title", "description", "thumbnail", "video_file"]
