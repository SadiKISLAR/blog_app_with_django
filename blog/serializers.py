from rest_framework import serializers
from django.db.models import Q
from .models import (
    Blog,
    Comment,
    Like,
    BlogView
    )

class LikeSerializer(serializers.ModelSerializer):

    user= serializers.StringRelatedField()
    user_id= serializers.IntegerField()
    blog= serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "user_id",
            "blog",
            "blog_id"
        )

class BlogSerializer(serializers.ModelSerializer):

    like = LikeSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "image" ,
            "category",
            "status" ,
            "published_date",
            "updated_date",
            "author",
            "like",
            "like_count",
            "has_liked",
            ]
        
    def get_like_count(self, obj):
        return obj.like.count()

    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Blog.objects.filter(Q(like__user=request.user) & Q(like__blog=obj)).exists():
                return True
            return False

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
        

class BlogViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogView
        fields = (
            "id",
            "user",
            "blog",
            "view_date",
        )