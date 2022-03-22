from .models import Comment, Post, Category
from django import forms

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


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
        fields = ('title', 'category', 'blog_snippet', 'content', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Choose a blog title!'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    """
    Form for editing blog posts.
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        populate fields when editing fields in a post.
        """
        model = Post
        fields = ('title', 'category',  'blog_snippet', 'content', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
