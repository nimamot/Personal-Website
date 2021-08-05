from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Linux

def home(request):
    return render(request, 'home.html')


def all_linux(request):
    linuxs = Linux.objects.order_by('-date')
    return render(request, 'linux/all_linux.html', {'linuxs':linuxs})


def detail(request, linux_id):
    linux = get_object_or_404(Linux, pk=linux_id)
    return render(request, 'linux/detail.html', {'linux':linux})
