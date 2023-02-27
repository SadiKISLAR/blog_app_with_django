from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

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
from .permissions import IsOwner

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(status="P")
    serializer_class = BlogSerializer
    # permission_classes [AllowAny,]
    
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, ]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        BlogView.objects.create(blog=instance, user=request.user)
        return Response(serializer.data)

class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(author=self.request.user)

class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsOwner]