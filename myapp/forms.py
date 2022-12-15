from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import Message
User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'image')
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ("content",)
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.fields['content'].widget.attrs["class"] = "content_field"


class UsernameChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username",)

class MailadressChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email",)

class IconChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("image",)