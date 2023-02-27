from django.db import models
from django.contrib.auth.models import User

blog_category = [
    ("i", "İnsan"),
    ("d", "Doğa"),
    ("y", "Yaşam"),
    ("s", "Sağlık"),
    ("t", "Teknoloji"),
]

blog_status = [
    ("D", "Draft"),
    ("P", "Published"),
]

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.URLField(blank='True')
    category = models.CharField(max_length=20, choices=blog_category)
    status = models.CharField(max_length=20, choices=blog_status, default="P")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(blank=True, unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.title

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.count()

    @property
    def get_view_count(self):
        return self.blogview_set.count()

    @property
    def get_like_count(self):
        return self.like.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Comment"

class BlogView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s View"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='like')

    def __str__(self):
        return f"{self.user.username}'s Like"


"""

Bu satır, Django'nun models modülü içerisinde yer alan SlugField sınıfından bir örnek oluşturarak, slug isimli bir alanı modelimize eklememizi sağlar.

SlugField, genellikle bir nesnenin benzersiz bir URL'sinde kullanılmak üzere tasarlanmış bir karakter dizisidir. Örneğin, bir blog gönderisinin URL'sinde kullanılacak bir slug, gönderinin başlığından veya başlıktaki bazı kelimelerin birleştirilmesiyle elde edilebilir. Slug alanının boş olabilmesi (blank=True) ve benzersiz olması (unique=True) belirtilmiştir.

Örneğin:

python
Copy code
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
Bu model, bir blog gönderisi için gereken temel alanları içermektedir. title alanı, gönderinin başlığını, content alanı ise gönderinin içeriğini depolamak için kullanılır. author alanı, gönderinin yazarını belirtirken, created_at ve updated_at alanları gönderinin ne zaman oluşturulduğunu ve son güncellendiğini takip eder. slug alanı ise gönderinin URL'sinde kullanılacak benzersiz karakter dizisini barındırır.

"""
