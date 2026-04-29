from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class AccountCreationForm(ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}), required=True)
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Create new password'}), required=True)
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'}), required=True)

    class Meta:
        model = USER_MODEL
        fields = ('profile_pic', 'first_name', 'last_name', 'email', 'about', 'username', 'password')

    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter a valid username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['about'].widget.attrs['class'] = 'text-area-field'
        # self.fields['profile_pic'].widget.attrs['style'] = None


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

    class Meta:
        model = USER_MODEL
        fields = ('username', 'password')

    def __init__(self):
        super(UserLoginForm, self).__init__()

        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['password'].widget.attrs['class'] = 'input-field'