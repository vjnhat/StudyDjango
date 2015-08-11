__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render
from django.core.serializers import json
from django.http import HttpResponse
from framgia.models.blog import Blog


def index(request):
    context = {}
    return render(request, 'index.html', context)



