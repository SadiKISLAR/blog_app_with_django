from django.urls import path, include
from rest_framework import routers

from .views import (
    BlogView,
    BlogDetailView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
