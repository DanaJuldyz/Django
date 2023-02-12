from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница")

def categories(request,catid):
    return HttpResponse(f"<h1>Косметика и ее виды</h1><p>{catid}</p>")

def not_found(request,exception):
    return HttpResponse("h1>404 Страница не найдена </h1>")