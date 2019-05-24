from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello')

def about(request):
    return HttpResponse('<em>Aboutttt</em>')
