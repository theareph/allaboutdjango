import json

from rest_framework.response import Response
from ipware import get_client_ip
from rest_framework.views import APIView
from . import utils

# Create your views here.


class WeatherAPIView(APIView):
    def get(self, request, *args, **kwargs):
        ip, is_routable = get_client_ip(request)
        ip, is_routable = "1.1.1.1", True
        if is_routable is False:
            return Response({"error": "access from local ip"})
        data = utils.get_weather(ip)
        location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return Response(
            {
                "location": location,
                "temp_c": temp_c,
                "condition": condition,
                "original_data": data,
            },
        )

class ServerDistroAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"distro": utils.get_distro()[0]})