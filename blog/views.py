from typing import ContextManager
from django.shortcuts import render

posts = [
    {
        'author': 'Anubhav',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'July 26, 2021',
    },

    {
        'author': 'Jan',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July 28, 2021',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
