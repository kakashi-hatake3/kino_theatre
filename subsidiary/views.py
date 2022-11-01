from django.shortcuts import render
from django.http import HttpResponse
from .models import Subsidiaryies


def index(request):
    cinemas = Subsidiaryies.objects.order_by('-pk')
    return render(request, 'subsidiary/index.html', {'subs': cinemas, 'title': 'Список кинотеатров'})


def subs_1(request):
    return HttpResponse('Кинотеатр 1')
