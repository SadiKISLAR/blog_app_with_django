from django.db import models
from django.contrib.auth.models import User


# Create your models here.

blog_category = [
    ("category_1", "İnsan"),
    ("category_2", "Doğa"),
    ("category_3", "Yaşam"),
    ("category_4", "Sağlık"),
    ("category_5", "Teknoloji"),
]

blog_status = [
    ("status_1", "Draft"),
    ("status_2", "Published"),
]

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    blog_pic = models.ImageField(blank='True')
    category = models.CharField(max_length=20, choices=blog_category)
    status = models.CharField(max_length=20, choices=blog_status)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

