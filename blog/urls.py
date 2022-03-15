# from . import views
from django.urls import path
from .views import (PostList, PostDetail, AddPostView, like_view, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, results_view)


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path('post-detial/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('like/<str:slug>', like_view, name='post_like'),
    path('post-detial/edit/<str:slug>/', EditPostView.as_view(), name='edit_post'),
    path('post-detial/<str:slug>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('search_blog', results_view, name='search_blog'),
]