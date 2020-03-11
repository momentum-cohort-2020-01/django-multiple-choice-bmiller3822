from django import forms

from .models import Snippet

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('snippet_title', 'description',
                 'category', 'code')