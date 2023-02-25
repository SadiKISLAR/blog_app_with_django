from rest_framework import serializers
from .models import (
    Blog,
    Comment,
    Like,
    BlogView
    )

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = [
            "id",
            "content",
            "image" ,
            "category",
            "status" ,
            "published_date",
            "updated_date",
            "slug" ,
            "author"
            ]

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

        fields = [
            "id",
            "user",
            "blog",
            "content",
            "publish_date"
        ]

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "blog",
        )
        

class BlogViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogView
        fields = (
            "id",
            "user",
            "blog",
            "view_date",
        )