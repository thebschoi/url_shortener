from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer
from django.views import generic
from .models import Url
import random

from my_url import serializers
from .forms import PostForm


@api_view(['POST'])
def my_url(request):
    # url이 DB에 이미 저장되어 있는 경우
    try:
        url = Url.objects.get(link=request.data["link"])
        serializer = UrlSerializer(url)
        return render(request, 'my_url/url_main.html', {'original_url':url.link, 'new_url':url.new_link})
    # 새로 들어온 url
    except:
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            temp_url = convert()
            new_link = settings.SITE_URL + temp_url
            serializer.save(new_link = new_link)
            return render(request, 'my_url/url_main.html', {'original_url':url.link, 'new_url':new_link})
    
def convert():
    encoding = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm',
                'n', 'o',' p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    while True:
        new_url = ''.join(random.sample(encoding, 8))
        try:
            url = Url.objects.get(new_link=new_url)
        except:
            return new_url

def original(request, new_url):
    new_link = settings.SITE_URL + new_url
    url = Url.objects.get(new_link=new_link)
    return HttpResponseRedirect(url.link)


def web_open(request):
    return render(request, 'my_url/url_main.html', {})
