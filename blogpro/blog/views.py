from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'abc',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'March 10, 2019'
    },

    {
        'author': 'xyz',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'March 11, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def base(request):
    return render(request, 'base.html', {'title': 'About'})


def login(request):
    return render(request, 'login.html', {})


def reg(request):
    return render(request, 'reg.html', {})


def blog1(re):
    return render(re, 'blog.html', {})


def blog2(re):
    return render(re, 'blog2.html', {})
