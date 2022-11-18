from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PostForm, ContactForm
from .models import Post, Project, Contact


def main(request):
    #return render(request, 'firstapp/main.html')
    return render(request, 'firstapp/closed.html')


def res(request):
    return render(request, 'firstapp/pri.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'firstapp/projects.html', {'projects': projects})


def contact1(request):
    return render(request, 'firstapp/contact.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.timeAdd = timezone.now()
            msg.save()
            form = ContactForm()
            #return redirect('firstapp.views.projects')
    else:
        form = ContactForm()
    return render(request, 'firstapp/contact.html', {'form': form})


def pnf(request, exception):
    context = {}
    context['page_title'] = '404'
    response = render(request, 'firstapp/404.html', context=context)
    response.status_code = 404
    return response
