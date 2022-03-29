import requests
import threading


def send():

    url = 'http://565km.xyz/'

    r = requests.get(url)

    print(r)

while(True):
    t1 = threading.Thread(target=send())
    t1.start()

