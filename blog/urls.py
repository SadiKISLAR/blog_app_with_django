from django.urls import path, include
from rest_framework import routers

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_detail'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_detail'),
]
