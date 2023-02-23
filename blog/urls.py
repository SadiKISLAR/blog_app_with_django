from django.urls import path, include
from .views import home
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('blog/', include(router.urls))
]
