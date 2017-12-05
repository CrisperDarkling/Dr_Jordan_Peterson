from django import forms
from .models import Post, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', "published_date")
        
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'content')