import json

from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip

from . import utils


# Create your views here.
def weather(request):
    ip, is_routable = get_client_ip(request)
    if is_routable is False:
        return HttpResponse("accessing from local ip")
    data = utils.get_weather(ip)
    location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    report= f"Weather report for {location}: {temp_c}C {condition}"
    return HttpResponse(report)
