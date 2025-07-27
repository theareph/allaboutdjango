from typing import override

from ipware import get_client_ip
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from . import models, serializers, utils

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


class DevlogPagination(PageNumberPagination):
    page_size = 3

class DevlogListAPIView(ListAPIView):
    serializer_class = serializers.DevlogSerializer
    pagination_class = DevlogPagination

    @override
    def get_queryset(self):
        return models.Devlog.objects.all()
