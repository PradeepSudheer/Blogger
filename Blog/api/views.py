from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Blog.models import Blogpost
from Blog.api.serializers import BlogpostSerializer

@api_view(['GET',])
def api_detail_blog_view(request, blog_id):
    try:
        blog_post = Blogpost.objects.get(id=blog_id)
    except Blogpost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BlogpostSerializer(blog_post)
        return Response(serializer.data)
