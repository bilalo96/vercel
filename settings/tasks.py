from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


def send_mail_task(subject,name,email,message):
    send_mail(
        subject,
        f'message from {name}\n email:{email}\n Message:{message},\n subject:{subject} ',
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )