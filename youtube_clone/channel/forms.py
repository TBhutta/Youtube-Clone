from django.forms import ModelForm
from django import forms
from .models import Video
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ["title", "description", "thumbnail", "video_file", "type", "restriction", "visibility"]

# TODO: Make a view to update an account
class AccountUpdateForm(ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}), required=True)
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}), required=True)
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid username'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}), required=True)

    class Meta:
        model = USER_MODEL
        # TODO: Add fields from User model
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_pic', 'about']