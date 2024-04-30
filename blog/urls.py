from django.urls import path
from .views import index, about, articles, article_detail, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', articles, name='articles'),
    path('contact/', contact, name='contact'),
    path('blog/<int:pk>/', article_detail, name='blog-detail'),

]
