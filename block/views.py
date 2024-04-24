from django.shortcuts import render
from .models import Post


# Create your views here.

def home_view(request):
    posts = Post.objects.all().order_by('id')
    context = {'posts': posts}
    return render(request, 'base.html', context)
