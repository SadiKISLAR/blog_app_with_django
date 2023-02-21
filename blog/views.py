from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    form = BlogForm()
    context = {
        'blogs' : blogs,
        'form' : form
    }
    return render(request, context)