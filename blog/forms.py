from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'name', 'post_text',)
        widgets = {
          'author': forms.Textarea(attrs={'rows':1, 'cols':20}),
          'name': forms.Textarea(attrs={'rows':1, 'cols':20}),
          'post_text': forms.Textarea(attrs={'rows':12, 'cols': 70}),
        }