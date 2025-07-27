import os
import typing as t

import requests
from django.core.cache import cache


def get_weather(ip: str) -> dict[str, t.Any]:
    key = os.environ.get("WEATHERAPI_KEY")
    if not key:
        raise ValueError("env var WEATHERAPI_KEY not set")
    cache_key = f"weatherapi-cache:{ip}"
    if cache.get(cache_key):
        return cache.get(cache_key)

    resp = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={ip}")
    result = resp.json()
    cache.set(cache_key, result, 3600)
    return result
