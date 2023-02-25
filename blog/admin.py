from django.contrib import admin
from .models import (
    Blog,
    BlogView,
    Like,
    Comment,
    )

admin.site.register(Blog)
admin.site.register(BlogView)
admin.site.register(Like)
admin.site.register(Comment)
