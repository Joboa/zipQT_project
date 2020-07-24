from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'zipQT/home.html')

def help(request):
    return render(request, 'zipQT/help.html')


def convert(request):
    return render(request, 'zipQT/convert.html')