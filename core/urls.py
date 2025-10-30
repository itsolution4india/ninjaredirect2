from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('contacts/', views.contacts, name='contacts'),
    path('estateplanning/', views.estateplanning, name='estateplanning'),
    path('smartfinancial/', views.smartfinancial, name='smartfinancial'),
    path('estateplanning_main/', views.estateplanning_main, name='estateplanning_main'),
    path('smartfinance_main/', views.smartfinance_main, name='smartfinance_main'),
    path('funding/', views.funding, name='funding'),
    path('funding_main/', views.funding_main, name='funding_main'),

    path('blog-detail/', views.blog_detail, name='blog_detail'),

    path('', views.index, name='index'),
]
