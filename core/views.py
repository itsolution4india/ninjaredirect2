from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def blogs(request):
    return render(request,'blog.html')
def contacts(request):
    return render(request,'contact.html')
def blog_detail(request):
    return render(request, 'blog-detail.html')
def estateplanning(request):
    return render(request,"Estateplanning.html")
def estateplanning_main(request):
    return render(request,"Estateplanning_main.html")

def smartfinancial(request):
    return render(request,'SmartFinancial.html')


def smartfinance_main(request):
    return render(request,'SmartFinance_main.html')

def funding(request):
    return render(request,'Funding.html')

def funding_main(request):
    return render(request,'Funding_main.html')