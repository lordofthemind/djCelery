from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import sleepTime, sub, sendMailTask


def masterindex(request):
    sleepTime.delay(60)

    sub.delay(54, 6)

    sendMailTask.delay()

    return HttpResponse('all tasks are completed')
