from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

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
    

class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = get_object_or_404(Blog, id=request.data["blog_id"])
        like_queryset = Like.objects.filter(user=request.user, blog=obj)
        if like_queryset.exists():
            like_queryset[0].delete()
        else:
            Like.objects.create(user=request.user, blog=obj)   
        
        data = {
            "msg":"Like",
        }
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()