from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request, 'home.html', {'name':'hitesh'})

def about(request):
    return HttpResponse('<em>Aboutttt</em>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist)})
