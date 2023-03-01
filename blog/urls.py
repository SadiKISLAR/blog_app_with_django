from django.urls import path, include
from rest_framework import routers

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    LikeView,
    CommentView,
)

router = routers.DefaultRouter()
router.register("like", LikeView)
router.register("comment", CommentView)

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    # path('', include(router.urls)),
]

urlpatterns += router.urls