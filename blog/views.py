from django.shortcuts import render, get_object_or_404
from .models import Contact, Category, Tag, Team, Post, HappyClients
from .forms import ContactForm


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about(request):
    about1 = Team.objects.all()
    happy_clients = HappyClients.objects.all()
    context = {'about': about1, 'happy_clients': happy_clients}
    return render(request, 'about.html', context)


def articles(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def article_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    tags = Tag.objects.all()
    cats = Category.objects.all()
    resent_post = Post.objects.all().order_by('-created_at')[:3]
    tag = request.GET.get('tag')
    if tag:
        post = Post.objects.filter(tags__name__contains=tag)
    search = request.GET.get('search')
    if search:
        post = Post.objects.filter(title__icontains=search)
    context = {
        'post': post,
        'tags': tags,
        'cats': cats,
        'resent_post': resent_post,
    }
    return render(request, 'blog-single.html', context)
