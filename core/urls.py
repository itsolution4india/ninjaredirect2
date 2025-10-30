from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('contacts/', views.contacts, name='contacts'),
    path('estateplanning/', views.estateplanning, name='estateplanning'),
    path('estateplanning_main/', views.estateplanning_main, name='estateplanning_main'),
    path('blog-detail/', views.blog_detail, name='blog_detail'),

    path('', views.index, name='index'),
]
