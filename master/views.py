from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import sleepTime, sub


def masterindex(request):
    sleepTime.delay(60)

    sub.delay(54, 6)

    return HttpResponse('I am about to wakeup!!')
