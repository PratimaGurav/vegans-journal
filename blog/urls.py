# from . import views
from .views import (PostList, PostDetail, AddPostView)
from django.urls import path

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]