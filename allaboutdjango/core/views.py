import json

from django.http.response import JsonResponse
from django.shortcuts import render
from ipware import get_client_ip

from . import utils


# Create your views here.

def weather(request):
    ip, is_routable = get_client_ip(request)
    ip, is_routable = "1.1.1.1", True
    if is_routable is False:
        return JsonResponse({"error": "access from local ip"})
    data = utils.get_weather(ip)
    location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    return JsonResponse(
        {"location": location, "temp_c": temp_c, "condition": condition, "original_data": data},
    )
