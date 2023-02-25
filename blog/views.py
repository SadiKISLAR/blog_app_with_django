from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import (
    Blog,
    Like,
    BlogView,
    Comment
    )

from .serializers import (
    BlogSerializer,
    CommentSerializer,
    LikeSerializer,
    BlogViewSerializer,
)

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     BlogView.objects.create(blog=instance, user=request.user)
    #     return Response(serializer.data)