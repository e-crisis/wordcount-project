from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

from collections import defaultdict


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = defaultdict(int)
    for word in wordlist:
        worddictionary[word] += 1
    worddictionary = sorted(worddictionary.items(), key=itemgetter(1), reverse=True)
    return render(request, 'count.html', {"fulltext": fulltext, "count": len(wordlist), "worddictionary": worddictionary})
