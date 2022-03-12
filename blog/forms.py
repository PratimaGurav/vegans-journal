from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AddPostForm(forms.ModelForm):
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        Populate fields when creating a post.
        """
        model = Post
        fields = ('title', 'content', 'featured_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Choose a blog title!'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }        