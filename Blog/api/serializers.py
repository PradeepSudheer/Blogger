from rest_framework import serializers
from Blog.models import Blogpost

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['image','title','body',]