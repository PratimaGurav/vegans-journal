# from . import views
from django.urls import path
from .views import (PostList, PostDetail, AddPostView, like_view, EditPostView, DeletePostView)


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path('post-detial/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('like/<str:slug>', like_view, name='post_like'),
    path('post-detial/edit/<str:slug>/', EditPostView.as_view(), name='edit_post'),
    path('post-detial/<str:slug>/delete', DeletePostView.as_view(), name='delete_post'),
]