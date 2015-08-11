__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render
from django.core.serializers import json
from django.http.response import HttpResponse


def index(request):
    context = {}
    return render(request, 'contact/index.html', context)


def contact_post(request):
    if request.method == 'POST':
        response_data = {}
        response_data['mgs'] = 'Create post successful!'
        return HttpResponse(json.dumps(response_data),content_type="application/json")


def contact_update(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'Create post successful!'

        return HttpResponse(json.dumps(response_data),content_type="application/json")