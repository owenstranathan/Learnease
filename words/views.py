from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Word

import logging as Log

from .forms import LookupForm
# Create your views here.


def home(request):
    return render(request, "base.html")


def index(request):
    words = Word.objects.all()
    return render(request, "words/index.html", {'words': words})


def detail(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    return render(request, "words/detail.html", {"word": word})


def hsk(request, level):
    hsk = Word.objects.filter(hsk_level=level)
    return render(request,"words/index.html", {"words": hsk})

def total(request):
    total = len(Word.objects.all())
    payload = {"total_words" : total}
    return JsonResponse(payload)
