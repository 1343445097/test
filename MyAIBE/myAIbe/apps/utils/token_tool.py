# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 17:18
# @Author  : YangYin
# @File    : token_tool.py
# @Software: PyCharm

# from django.conf import settings
import jwt
import time

#编码token信息
def encode(user_info):
    now = time.time()
    dic = {'exp':now+5,
           'iat':now,    # 签发时间
           'iss':'myai',    # 签发者
           'data':user_info,
           'timestamp':now
           }
    token = jwt.encode(
        dic, 'myai',
        algorithm='HS256',
        headers={'typ': 'JWT', 'alg': 'HS256'}
    )
    return token

def decode(token):
    try:
        payload = jwt.decode(token, "myai", algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        print('token已失效')
        return False
    except jwt.DecodeError:
        print('token认证失败')
        return False
    except jwt.InvalidTokenError:
        print('非法的token')
        return False
if __name__=='__main__':
    a = encode({"name":"yangyin","secrect":"123"})
    print("3"+a+"1")
    time.sleep(2)
    decode("123")