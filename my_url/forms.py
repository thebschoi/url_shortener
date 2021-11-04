from django import forms
from .models import Url


class PostForm(forms.ModelForm):
    class Meta:
        model = Url
        #fields = '__all__'
        fields = ('link', 'new_link')