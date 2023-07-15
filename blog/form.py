from django import forms
from .models import PostComments

class CommentPostForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea ,max_length=1000)

    class Meta:
        model = PostComments
        fields = ['body']