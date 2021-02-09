from django import forms
from .models import ForumThread


class AddThreadForm(forms.ModelForm):
    heading = forms.CharField(max_length=100)
    content = forms.CharField(max_length=750)

    class Meta:
        model = ForumThread
        fields = ('heading', 'content')
