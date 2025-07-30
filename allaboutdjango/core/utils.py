import subprocess
import typing as t

import country_converter
import requests
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.core.cache import cache

cc = country_converter.CountryConverter()
g = GeoIP2()


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


def get_region(ip: str, method: t.Literal["weatherapi", "mmdb"] | None = None) -> str:
    if method is None:
        method = getattr(settings.CUSTOM_GEOIP_METHOD, "weatherapi")
    match method:
        case "weatherapi":
            country = get_weather(ip).get("location", {}).get("country", "Unknown")

            result = cc.convert(country, to="ISO2")
            if isinstance(result, list):
                return result[0]
            else:
                return result
        case "mmdb":
            return g.country(ip).get("country_code") or "Unknown"
        case _:
            return "Unknown"
