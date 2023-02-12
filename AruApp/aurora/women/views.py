from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница")

def categories(request,catid):
    return HttpResponse(f"<h1>Косметика и ее виды</h1><p>{catid}</p>")

def not_found(request,exception):
    return HttpResponse("h1>404 Страница не найдена </h1>")

def server_error(request,exception):
    return HttpResponse("h1>500 Ошибка сервера </h1>")

def Access_is_denied(request,exception):
    return HttpResponse("h1>403 Доступ запрещен </h1>")

def request_processing(request,exception):
    return HttpResponse("h1>400 Невозможно обработать запрос </h1>")
