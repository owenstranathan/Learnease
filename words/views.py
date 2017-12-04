from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse
from .models import Word

import logging

# Create your views here.


logger = logging.getLogger(__name__)


def lookup(request):
    pass


# loads a static template under introduction
# grabs the right template based on the page name
def introduction(request, page_name):
    if page_name == "":
        page_name = "index"
    template = "introduction/{0}.html".format(page_name)
    return render(request, template)


def home(request):
    return render(request, "home.html")


def pinyin(request):
    return render(request, "pinyin.html")


def index(request):
    words = Word.objects.all()
    return render(request, "words/index.html", {'words': words})


def detail(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    return render(request, "words/detail.html", {"word": word})


def hsk(request, level):
    hsk = Word.objects.filter(hsk_level=level)
    payload = {
        'level': level,
        'words': hsk,
    }
    return render(request, "words/hsk.html", payload)


def total(request):
    total = len(Word.objects.all())
    payload = {"total_words" : total}
    return JsonResponse(payload)
