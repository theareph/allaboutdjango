import os
import subprocess
import typing as t

import requests
from django.core.cache import cache

from django.conf import settings

def get_weather(ip: str) -> dict[str, t.Any]:
    key = settings.WEATHERAPI_KEY
    if not key:
        raise ValueError("env var WEATHERAPI_KEY not set")
    cache_key = f"weatherapi-cache:{ip}"
    if cache.get(cache_key):
        return cache.get(cache_key)

    resp = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={ip}")
    result = resp.json()
    cache.set(cache_key, result, 3600)
    return result


def shell_run(command: str):
    return subprocess.run(command.split(), capture_output=True, text=True)


def get_distro() -> tuple[str, str]:
    """
    returns (distro_id, version)
    """
    entries = shell_run("lsb_release -a").stdout.split("\n")
    entries = filter(lambda s: bool(s), entries)
    data = {}
    for entry in entries:
        key, value = entry.split(":")
        data[key.strip()] = value.strip()
    return data["Distributor ID"], data["Release"]
