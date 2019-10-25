from django.urls import path
from Blog.api.views import api_detail_blog_view

app_name = 'blog'

urlpatterns=[
    path('blogpost/<int:blog_id>/', api_detail_blog_view, name='detail')
]