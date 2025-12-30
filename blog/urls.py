from django.urls import path
from .views import blog_view,blog_detail_view

app_name = 'blog'
urlpatterns = [
    path('',blog_view,name='blog_index'),
    path('sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssblog-detail', blog_detail_view, name='blog_detail'),
]