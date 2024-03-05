import re
import socket
from bs4 import BeautifulSoup
import requests


def status_check(url):
    with requests.Session() as session:
        response = session.get(url).status_code
        if response == 200:
            print('Сайт работает')
        else:
            print('Сайт не работает, или к нему нет доступа')
        return response


def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url[7:])
        print(f'HOST NAME: {url}\nHOST IP: {ip_address}')
        return ip_address
    except socket.gaierror as error:
        print(f'IP не читается из-за ошибки: {error}')


def get_phone_number(url):
    with requests.Session() as session:
        response = session.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        phone_number = soup.find(class_='phone-number').text
        result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                          phone_number)
        if bool(result):
            print('Tel:', phone_number)
            return phone_number
        print(f'Номер {phone_number} - некорректен')
