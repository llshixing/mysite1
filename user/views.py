from django.http import HttpResponse
from user import models
import json
import pymysql

def userLogin(request):
    login_msg = request.GET
    print(login_msg['username'])
    user = getUser(login_msg['username'])
    if user:
        print(user.password)
        if user.password == login_msg['password']:
            print('dengluchewngong')
            return HttpResponse('登录成功')
        else:
            return HttpResponse('密码不正确')
    return HttpResponse('用户不存在')


def getUser(login_username):
    try:
        user = models.User.objects.get(userName=login_username)
    except:
        return ""
    return user
