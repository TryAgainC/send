import requests
import random
import threading

def regist():
    url = "https://latiao.club/api/v1/passport/auth/register"
    qq_num = random.randint(1,9999999999)

    qq_email = "%d@qq.com" % qq_num

    qq_password = random.randint(100000000,999999999999)

    data = {
        "email": qq_email,
        "password": qq_password,
        'invite_code': 'i0DrByrY'
    }

    r = requests.post(url=url,data=data)
    print(qq_email,qq_password,r)


while(True):
    t1 = threading.Thread(target=regist())
    t1.start()






