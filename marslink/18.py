import requests
import threading


def send():

    url = 'https://ss.marslink.org/#/login'

    r = requests.get(url)

    print(r)

while(True):
    t1 = threading.Thread(target=send())
    t1.start()

