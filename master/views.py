from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import sleepTime


def masterindex(request):
    sleepTime.delay(15)
    return HttpResponse('I am about to wakeup!!')
