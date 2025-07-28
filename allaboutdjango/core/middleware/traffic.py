from ipware import get_client_ip
from django.http.response import HttpResponse
class BlockExternalTrafficMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        from django.conf import settings
        block_external_traffic = getattr(settings, "BLOCK_EXTERNAL_TRAFFIC", False)
        if block_external_traffic:
            _, is_routable = get_client_ip(request)
            if is_routable is True:
                return HttpResponse("403 Forbidden", status=403)
        response  = self.get_response(request)
        return response