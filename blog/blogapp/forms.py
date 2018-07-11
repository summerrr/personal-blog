from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']
       # labels={'text':''}
        widgets={'body':forms.Textarea(attrs={'cols':80})}
