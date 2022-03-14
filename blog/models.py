from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Publish"))

class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        This fixes an error which the button on add categories
        is not taking user back as expected.
        """
        return reverse('home')
    


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('post_detail', kwargs=kwargs)    

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        """
        This fixes an error which the button on add blog post
        is not taking user back as expected.
        """
        return reverse('home')


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

        