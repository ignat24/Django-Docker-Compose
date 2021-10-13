from django.http import HttpResponse


def log_in(request):
    return HttpResponse('<h1> You are was login <h1>')


def sign_up(request):
    return HttpResponse('<h1> You are was sign_up <h1>')