# from . import views
from django.urls import path
from .views import (PostList, PostDetail, AddPostView)


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path('post-detial/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]