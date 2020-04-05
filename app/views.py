from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def hello(request):
    return render(request,'base.html',{
        'questions': range(6),
    })
