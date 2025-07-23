import os
import typing as t

import requests


def get_weather(ip: str) -> dict[str, t.Any]:
    key = os.environ.get("WEATHERAPI_KEY")
    resp = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={ip}")
    return resp.json()
