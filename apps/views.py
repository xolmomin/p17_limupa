from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from apps.forms import RegisterForm
from apps.models import Blog, Category


def blog_list_page(request):
    context = {
        'blogs': Blog.objects.all().order_by('-created_at')
    }
    return render(request, 'apps/blogs/blog-list.html', context)


def blog_detail_page(request, pk):
    context = {
        'blog': Blog.objects.filter(pk=pk).first(),
        'categories': Category.objects.all()
    }
    return render(request, 'apps/blogs/blog-detail.html', context)


def index_page(request):
    return render(request, 'apps/index.html')


def logout_page(request):
    logout(request)
    return redirect('index_page')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')

    return render(request, 'apps/login.html')


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_page')

    return render(request, 'apps/login.html')
