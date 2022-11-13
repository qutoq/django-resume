from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Project


def main(request):
    #return render(request, 'firstapp/main.html')
    return render(request, 'firstapp/closed.html')


def res(request):
    return render(request, 'firstapp/pri.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'firstapp/projects.html', {'projects': projects})


def contact(request):
    return render(request, 'firstapp/contact.html')


def pnf(request, exception):
    context = {}
    context['page_title'] = '404'
    response = render(request, 'firstapp/404.html', context=context)
    response.status_code = 404
    return response