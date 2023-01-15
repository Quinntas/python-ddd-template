from functools import cache

import requests


@cache
def get_ip_info(ip: str, token: str) -> list:
    url = f"https://ipinfo.io/{ip}?token={token}"
    return requests.get(url).json()
