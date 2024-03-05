import socket

from requests import request


def status_check(url):
    response = request.get(url).status_code
    return response


def get_ip_address(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def get_phone_number(url):
