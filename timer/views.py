from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime, time
import json

def timefetch(request):
    now = datetime.datetime.now()
    unix = time.mktime(now.timetuple())*1000

    json = {}
    json['date'] = now
    json['unix'] = unix
    return JsonResponse(json)