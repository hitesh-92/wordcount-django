from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'name':'hitesh'})

def about(request):
    # return HttpResponse('<em>Aboutttt</em>')
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    dictionary = {}

    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    data = {
    'fulltext': fulltext,
    'count': len(wordlist),
    'dictionary': sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    }

    # return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'dictionary': dictionary.items()})
    return render(request, 'count.html', data)
