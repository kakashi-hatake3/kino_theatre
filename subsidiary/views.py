from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Кинотеатры(филиалы) по городу')


def subs_1(request):
    return HttpResponse('Кинотеатр 1')
