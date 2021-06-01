from django.shortcuts import render

from django.http import HttpResponse

def registr(request):
    return HttpResponse("register")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")

def not_define(request):
    return HttpResponse("unavailable")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})