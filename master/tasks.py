from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepTime(total_time):
    sleep(total_time)
    return None


@shared_task
def sub(x, y):
    
    return x - y


@shared_task
def sendMailTask():
    
    sleep(15)


    subject = 'Celery mail django'
    message = 'Body of the email.'
    from_email = 'Happy.Birthday270821@gmail.com'
    recipient_list = ['supermanishkeshav98@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return None


