import requests
import random
import time
import threading

def regist():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}
    url = "https://nivpn.com/api/v1/passport/auth/register"
    qq_num = random.randint(1,9999999999)

    qq_email = "%d@qq.com" % qq_num

    qq_password = random.randint(100000000,999999999999)

    data = {
        "email": qq_email,
        "password": qq_password
    }

    r = requests.post(url=url,data=data,headers=headers)
    print(qq_email,qq_password,r)


while(True):
    t1 = threading.Thread(target=regist())
    t1.start()








