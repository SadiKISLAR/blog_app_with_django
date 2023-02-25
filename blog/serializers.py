from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = [
            "content",
            "image" ,
            "category",
            "status" ,
            "published_date",
            "updated_date",
            "slug" ,
            "author"]

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

        fields = [
            "user",
            "blog",
            "content",
            "publish_date"
        ]


